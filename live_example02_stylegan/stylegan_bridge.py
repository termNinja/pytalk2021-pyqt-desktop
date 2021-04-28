import os

import PIL.Image
import numpy as np
import torch
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui

import dnnlib
import legacy


class StyleGanBridge(QtCore.QThread):

    def __init__(self, parent=None):
        super(StyleGanBridge, self).__init__(parent)

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

    def run(self):
        self._init_model()
        while True:
            pass
