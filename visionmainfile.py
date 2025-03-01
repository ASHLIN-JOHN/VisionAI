from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NARUTOAIUI(object):
    def setupUi(self, NARUTOAIUI):
        NARUTOAIUI.setObjectName("NARUTOAIUI")
        NARUTOAIUI.resize(1280, 720)
        NARUTOAIUI.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "")

        self.logo = QtWidgets.QLabel(NARUTOAIUI)
        self.logo.setGeometry(QtCore.QRect(390, -70, 461, 461))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\NARUTO\\gui\\uzumkai logo.gif"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.terminalbox = QtWidgets.QTextEdit(NARUTOAIUI)
        self.terminalbox.setGeometry(QtCore.QRect(10, 290, 1111, 371))
        self.terminalbox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                        "font: 20pt \"Agency FB\";\n"
                                        "color: white;\n"  # Added to make the text color white
                                        "background-color: transparent;\n"
                                        "border-width:3px 3px 3px 3px;\n"
                                        "border-style:solid;\n"
                                        "")
        self.terminalbox.setObjectName("terminalbox")

        self.commandbox = QtWidgets.QLineEdit(NARUTOAIUI)
        self.commandbox.setGeometry(QtCore.QRect(10, 660, 1111, 51))
        self.commandbox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                       "background-color: transparent;\n"
                                       "border-width:3px 3px 3px 3px;\n"
                                       "border-style:solid;\n"
                                       "font: 19pt \"Agency FB\";\n"
                                       "color: white;"  # Added to make the text color white
                                       "")
        self.commandbox.setObjectName("commandbox")

        self.startbutton = QtWidgets.QPushButton(NARUTOAIUI)
        self.startbutton.setGeometry(QtCore.QRect(990, 640, 141, 91))
        self.startbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startbutton.setStyleSheet("border-image: url(D:/NARUTO/gui/start.png);\n"
                                       "background-color: transparent;")
        self.startbutton.setText("")
        self.startbutton.setObjectName("startbutton")

        self.exitbutton = QtWidgets.QPushButton(NARUTOAIUI)
        self.exitbutton.setGeometry(QtCore.QRect(1130, 640, 141, 91))
        self.exitbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitbutton.setStyleSheet("border-image: url(D:/NARUTO/gui/exit.png);\n"
                                      "background-color: transparent;")
        self.exitbutton.setText("")
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(NARUTOAIUI)
        QtCore.QMetaObject.connectSlotsByName(NARUTOAIUI)

    def retranslateUi(self, NARUTOAIUI):
        _translate = QtCore.QCoreApplication.translate
        NARUTOAIUI.setWindowTitle(_translate("Vision AI", "Vision AI"))
        self.commandbox.setPlaceholderText(_translate("NARUTOAIUI", " ENTER YOUR COMMAND:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    NARUTOAIUI = QtWidgets.QWidget()
    ui = Ui_NARUTOAIUI()
    ui.setupUi(NARUTOAIUI)
    NARUTOAIUI.show()
    sys.exit(app.exec_())
