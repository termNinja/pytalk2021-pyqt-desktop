import os

import PIL.Image
import numpy as np
import torch
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PIL.ImageQt import ImageQt

import dnnlib
import legacy


class StyleGanBridge(QtCore.QThread):

    # Signal which we shall emit once our generated image is complete!
    result_ready = QtCore.pyqtSignal(QtGui.QPixmap)

    def __init__(self, parent=None):
        super(StyleGanBridge, self).__init__(parent)
        self.seed = None
        self.should_generate = False
        self._mutex = QtCore.QMutex()

    @pyqtSlot(int)
    def receive_gen_request(self, seed):
        """
        Handles the image generation request. It receives a seed which
        we forward to the network so it can start the image generation process.
        """
        print(f'[{QtCore.QThread.currentThreadId()}] Received gen request for seed {seed}')
        self.seed = seed
        self.set_state_should_generate_atomic(True)

    def _init_model(self):
        """
        Initializes the StyleGAN model. You don't need to look at this really :)
        """
        network_pkl = 'https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/afhqdog.pkl'
        print('Loading networks from "%s"...' % network_pkl)
        device = torch.device('cuda')
        with dnnlib.util.open_url(network_pkl) as f:
            self.G = legacy.load_network_pkl(f)['G_ema'].to(device)  # type: ignore
        self.outdir = 'out'
        os.makedirs(self.outdir, exist_ok=True)
        self.label = torch.zeros([1, self.G.c_dim], device=device)
        self.truncation_psi = 1
        self.noise_mode = 'const'
        print('Model ready!')

    def generate(self):
        """
        Generates the image and emits a signal with the generated image.
        """
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        z = torch.from_numpy(np.random.RandomState(self.seed).randn(1, self.G.z_dim)).to(device)
        img = self.G(z, self.label, truncation_psi=self.truncation_psi, noise_mode=self.noise_mode)
        img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
        generated_image = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')

        # In case you want to save generated images :)
        # generated_image.save(f'{self.outdir}/seed{self.seed:04d}.png')

        # convert Pillow Image to QPixmap
        qim = ImageQt(generated_image)
        pix = QtGui.QPixmap.fromImage(qim)

        # Emit the signal that the image is generated and send it!
        self.result_ready.emit(pix)

    def set_state_should_generate_atomic(self, state: bool):
        self._mutex.lock()
        self.should_generate = state
        self._mutex.unlock()

    def run(self):
        self._init_model()
        while True:
            if self.should_generate:
                print(f'[{QtCore.QThread.currentThreadId()}] Generating image for seed {self.seed}')
                self.generate()
                print(f'[{QtCore.QThread.currentThreadId()}] Generated image for seed {self.seed}')
                self.set_state_should_generate_atomic(False)
