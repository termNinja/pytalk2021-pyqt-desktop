from PyQt5 import QtGui
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import *

from MainWindow import Ui_MainWindow
from example01_slack_msg.slack_controller import SlackController


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
        self.slack_controller: SlackController = None
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
        self.slack_controller: SlackController = SlackController(token)
        if self.slack_controller.status['ok']:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Connection information")
            msg.setText("Connection success!")
            msg.exec_()
            self.gbChannels.setEnabled(True)
            self.gbMessage.setEnabled(True)
            model = QtGui.QStandardItemModel()
            self.lvChannels.setModel(model)
            for conv in self.slack_controller.conversations:
                item = QtGui.QStandardItem(conv.name)
                model.appendRow(item)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Connection information")
            msg.setText("Connection failed!")
            msg.setDetailedText(self.slack_controller.status['error'])
            msg.exec_()

    def handle_send(self):
        q_model_index: QModelIndex = self.lvChannels.currentIndex()
        i = q_model_index.row()
        target_conversation = self.slack_controller.conversations[i]
        msg = self.teMsg.toPlainText()
        self.slack_controller.send_msg_to_channel(msg, target_conversation.id)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("SlackMsg")

    window = MainWindow()

    app.exec_()
