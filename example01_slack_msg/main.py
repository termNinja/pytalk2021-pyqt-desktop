from PyQt5.QtWidgets import *

from MainWindow import Ui_MainWindow
from example01_slack_msg.SlackMsg import SlackMsgDispatcher


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Constructs the application main window.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.set_event_handlers()

        # TODO -> Properly read channels -> demonstrate Qt list model-view here
        # TODO -> Properly read users
        # TODO -> Properly set token, channels and users
        self.slack_msg = SlackMsgDispatcher("xoxb-2008514871233-1992851393701-L1KVcgB02FaIAcoOsLVp1RFw")
        self.target_channel = "C01VA397NCT"

        self.show()

    def set_event_handlers(self):
        self.actionQuit.triggered.connect(self.handle_quit)
        self.pbSend.clicked.connect(self.handle_send)

    def handle_quit(self):
        self.app.quit()

    def handle_send(self):
        # Parse token
        msg = self.teMsg.toPlainText()
        self.slack_msg.send_msg_to_channel(msg, self.target_channel)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("SlackMsg")

    window = MainWindow()

    app.exec_()
