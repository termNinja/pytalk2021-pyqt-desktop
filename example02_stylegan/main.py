from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from MainWindow import Ui_MainWindow
from example02_stylegan.stylegan_bridge import StyleGanBridge

import random


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Constructs the application main window.
    """

    generate_for_seed = QtCore.pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_event_handlers()

        # Load icon image from QResources file. We use `import resources` to accomplish this.
        self.setWindowIcon(QtGui.QIcon(':/icon'))

        self.thread = StyleGanBridge()
        self.thread.start()

        self.generate_for_seed.connect(self.thread.receive_gen_request)
        self.thread.result_ready.connect(self.receive_generated_image)

        self.show()

    @pyqtSlot(QtGui.QPixmap)
    def receive_generated_image(self, generated_image: QtGui.QPixmap):
        self.lblImage.setPixmap(generated_image)

    def set_event_handlers(self):
        self.pbGenerate.clicked.connect(self.handle_generate)
        self.pbGenerateRandom.clicked.connect(self.handle_generate_random)
        self.pbTheEnd.clicked.connect(self.handle_the_end)

    def handle_generate_random(self):
        random_seed = random.randint(1, 1000)
        self.leSeed.setText(str(random_seed))
        self.generate_for_seed.emit(random_seed)

    def handle_generate(self):
        seed = self.leSeed.text()
        self.generate_for_seed.emit(int(seed))

    def handle_the_end(self):
        self.lblImage.setPixmap(QtGui.QPixmap(':/the_end'))


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("StyleGAN <3")

    window = MainWindow()

    app.exec_()
