from PyQt5.QtWidgets import *

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Constructs the application main window.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("SlackMsg")

    window = MainWindow()

    app.exec_()
