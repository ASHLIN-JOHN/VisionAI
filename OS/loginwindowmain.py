import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from loginwindow import Ui_loginWindowClass
from PyQt5 import QtGui
from VisonAI import Ui_NARUTO
from subprocess import call
import speech_recognition as sr

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print("SETTING UP YOUR AI SIR")
        self.loginUI = Ui_loginWindowClass()
        self.loginUI.setupUi(self)

        self.loginUI.accessdenied.hide()
        self.loginUI.password.setEchoMode(QLineEdit.Password)

        self.loginUI.accessdeniedMovie = QtGui.QMovie("D:\\NARUTO AI\\QT\\loginWindowClass\\GUI KEYS\\ACCDSS DEN.gif")
        self.loginUI.accessdenied.setMovie(self.loginUI.accessdeniedMovie)

        self.loginUI.exitbutton.clicked.connect(self.close)
        self.loginUI.retrybutton.clicked.connect(self.retryButton)
        self.loginUI.loginbutton.clicked.connect(self.validatelogin)

    def startMovie(self):
        self.loginUI.accessdenied.show()
        self.loginUI.accessdeniedMovie.start()

    def stopMovie(self):
        self.loginUI.accessdenied.hide()
        self.loginUI.accessdeniedMovie.start()

    def retryButton(self):
        self.loginUI.username.clear()
        self.loginUI.password.clear()
        self.stopMovie()

    def validatelogin(self):
        username = self.loginUI.username.text()
        password = self.loginUI.password.text()
        if username == "ashlin" and password == "!@#$":
            print("SETTING UP YOUR AI")
            self.connectloginwin()
        else:
            self.startMovie()

    def connectloginwin(self):
        self.close()
        call(["python", "VisionAI.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LoginWindow()
    ui.show()
    sys.exit(app.exec_())
