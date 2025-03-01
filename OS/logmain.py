from PyQt5 import QtGui
from VisionAI import UI_Naruto
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from loginwindow import Ui_loginWindowClass

class loginmain():
    def __init__(self):
        super(loginmain, self).__init__()
        print("SETTING UP GUI")
        self.loginUI = UI_Naruto()
        self.loginUI.setupUi(self)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginmain()
    ui.show()
    sys.exit(app.exec_())