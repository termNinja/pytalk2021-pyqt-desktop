# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblSlackToken = QtWidgets.QLabel(self.centralwidget)
        self.lblSlackToken.setObjectName("lblSlackToken")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSlackToken)
        self.leSlackToken = QtWidgets.QLineEdit(self.centralwidget)
        self.leSlackToken.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSlackToken.setObjectName("leSlackToken")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leSlackToken)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.teMsg = QtWidgets.QTextEdit(self.groupBox)
        self.teMsg.setObjectName("teMsg")
        self.gridLayout.addWidget(self.teMsg, 1, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.pbSend = QtWidgets.QPushButton(self.centralwidget)
        self.pbSend.setObjectName("pbSend")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pbSend)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblSlackToken.setText(_translate("MainWindow", "Slack Token"))
        self.groupBox.setTitle(_translate("MainWindow", "Message"))
        self.pbSend.setText(_translate("MainWindow", "Send"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
