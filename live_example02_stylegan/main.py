from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from MainWindow import Ui_MainWindow


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

        # self.thread = StyleGanBridge()
        # self.thread.start()

        # self.generate_for_seed.connect(self.thread.receive_gen_request)
        # self.thread.result_ready.connect(self.receive_generated_image)

        self.show()

    def set_event_handlers(self):
        self.pbGenerate.clicked.connect(self.handle_generate)
        self.pbGenerateRandom.clicked.connect(self.handle_generate_random)
        self.pbTheEnd.clicked.connect(self.handle_the_end)

    def handle_generate_random(self):
        # TODO
        pass

    def handle_generate(self):
        # TODO
        pass

    def handle_the_end(self):
        self.lblImage.setPixmap(QtGui.QPixmap(':/the_end'))


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("StyleGAN <3")

    window = MainWindow()

    app.exec_()
