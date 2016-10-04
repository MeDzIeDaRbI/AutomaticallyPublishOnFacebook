# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\faceAuto\gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import thread

import time
from PyQt4 import QtCore, QtGui
import pyautogui
import win32api
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(465, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-710, 0, 1361, 421))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://www.facebook.com/")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 430, 461, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 50, 41, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 41, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(400, 50, 51, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 20, 51, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 41, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 20, 41, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 20, 51, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 20, 51, 51))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 20, 51, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_5"))
        self.webView.raise_()
        self.webView.raise_()
        self.webView.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.right)
        self.pushButton_2.clicked.connect(self.left)
        self.pushButton_3.clicked.connect(self.up)
        self.pushButton_4.clicked.connect(self.down)
        self.pushButton_5.clicked.connect(self.connect)
        self.pushButton_6.clicked.connect(self.shatreThread)

    def go2Page(self):
        #self.webView.setUrl())
        #self.webView.load(QtCore.QUrl(_fromUtf8("https://www.facebook.com/gottawatch/")))
        self.webView.load(QtCore.QUrl(_fromUtf8("https://google.com")))
    def shatreThread(self):
        thread.start_new_thread(self.share,('Thread',))
    def share(self, name):
        x = self.webView.geometry()
        x.adjust(0, 0, 18*50, 0)
        self.webView.setGeometry(x)
        time.sleep(2)
        x = pyautogui.locateOnScreen(r'D:\Projects\faceAuto\a2.PNG')
        pyautogui.click(x[0],x[1])
        pyautogui.typewrite('This is a selenium use case')
        x = pyautogui.locateOnScreen(r'D:\Projects\faceAuto\a3.PNG')
        pyautogui.click(x[0],x[1])



        pass
    def left(self):
        x = self.webView.geometry()
        x.adjust(0, 0, 50, 0)
        self.webView.setGeometry(x)

    def right(self):
        x = self.webView.geometry()
        x.adjust(0, 0, -50, 0)
        self.webView.setGeometry(x)

    def up(self):
        x = self.webView.geometry()
        x.adjust(0, 0, 0, 10)
        self.webView.setGeometry(x)

    def down(self):
        x = self.webView.geometry()
        x.adjust(0, 0, 0, -10)
        self.webView.setGeometry(x)

    def connect(self):
        #win32api.LoadKeyboardLayout('00000409', 1)  # to switch to english
        thread.start_new_thread(self.connThread,('Thread',))
        time.sleep(2)
        #win32api.LoadKeyboardLayout('00002060', 1)  # to switch to french

    def connThread(self,name):
        log = "addValidUsername@validusername.com"

        passw = "3.1424578"
        x = pyautogui.locateOnScreen(r'D:\Projects\faceAuto\a1.PNG')
        recPos = pyautogui.position()
        pyautogui.click(x[0] + 20, x[1] - 380)
        pyautogui.typewrite(log)

        pyautogui.click(x[0] + 200, x[1] - 380)
        pyautogui.typewrite(passw)
        #pyautogui.click(x[0] + 420, x[1] - 380)
        pyautogui.moveTo(recPos)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Console", None))
        self.pushButton_2.setText(_translate("MainWindow", "left", None))
        self.pushButton.setText(_translate("MainWindow", "right", None))
        self.pushButton_3.setText(_translate("MainWindow", "up", None))
        self.pushButton_4.setText(_translate("MainWindow", "down", None))
        self.pushButton_5.setText(_translate("MainWindow", "Connect", None))
        self.pushButton_6.setText(_translate("MainWindow", "Share", None))
        self.pushButton_7.setText(_translate("MainWindow", "GoPage", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

