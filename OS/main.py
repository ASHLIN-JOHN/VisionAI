import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui
from mainGUIFile import Ui_Dialog
import loginwindowmain

class mainfile(QDialog):
    def __init__(self):
        super(mainfile, self).__init__()
        print("LOGIN TO START THE AI SIR")
        self.firstUI = Ui_Dialog()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("D:\\NARUTO AI\\LOGO\\uzumkai logo.gif")
        self.firstUI.uzumakilogo.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.loginbutton.clicked.connect(self.connectloginwin)
        self.firstUI.exitbutton.clicked.connect(self.close)

    def connectloginwin(self):
        self.close()
        self.login = loginwindowmain.LoginWindow()
        self.login.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainfile()
    ui.show()
    sys.exit(app.exec_())
