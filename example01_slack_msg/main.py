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
        self.slack_msg: SlackMsgDispatcher = None
        self.target_channel = "C01VA397NCT"

        self.gbChannels.setEnabled(False)
        self.gbMessage.setEnabled(False)

        self.show()

    def set_event_handlers(self):
        self.actionQuit.triggered.connect(self.handle_quit)
        self.pbSend.clicked.connect(self.handle_send)
        self.pbConnect.clicked.connect(self.handle_connect)

    def handle_quit(self):
        self.app.quit()

    def handle_connect(self):
        token = self.leSlackToken.text()
        self.slack_msg: SlackMsgDispatcher = SlackMsgDispatcher(token)
        if self.slack_msg.status['ok']:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Connection information")
            msg.setText("Connection success!")
            msg.exec_()
            self.gbChannels.setEnabled(True)
            self.gbMessage.setEnabled(True)
            resp = self.slack_msg.list_channels()
            for c in resp:
                print(c)
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Connection information")
            msg.setText("Connection failed!")
            msg.setDetailedText(self.slack_msg.status['error'])
            msg.exec_()

    def handle_send(self):
        # Parse token
        msg = self.teMsg.toPlainText()
        self.slack_msg.send_msg_to_channel(msg, self.target_channel)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("SlackMsg")

    window = MainWindow()

    app.exec_()
