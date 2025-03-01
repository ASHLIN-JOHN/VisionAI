import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QIntValidator
from OS.contactsfile import Ui_ContactFile
from PyQt5 import QtGui, QtCore


class ContactWindow(QWidget):
    def __init__(self, contacts_path):
        super(ContactWindow, self).__init__()
        self.contactUI = Ui_ContactFile()
        self.contactUI.setupUi(self)

        self.contacts_path = contacts_path

        self.onlyInt = QIntValidator()
        self.contactUI.numberline.setValidator(self.onlyInt)

        self.contactUI.savebutton.clicked.connect(self.save_contact)
        self.contactUI.cancelbutton.clicked.connect(self.close)

    def save_contact(self):
        name = self.contactUI.nameline.text()
        number = self.contactUI.numberline.text()
        if name and number and len(number) == 10 and number.isdigit():
            with open(self.contacts_path, 'a') as file:
                file.write(f"'{name}: {number}',\n")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Contact saved successfully!")
            msg_box.setWindowTitle("Success")
            msg_box.addButton(QMessageBox.Ok)
            msg_box.exec_()
            self.close()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            if not name:
                msg_box.setText("Please enter name!")
            elif not number:
                msg_box.setText("Please enter number!")
            elif len(number) != 10:
                msg_box.setText("Phone number should be 10 digits long!")
            elif not number.isdigit():
                msg_box.setText("Phone number should contain only digits!")
            msg_box.setWindowTitle("Error")
            msg_box.addButton(QMessageBox.Retry)
            msg_box.exec_()


if __name__ == "__main__":
    contacts_path = "D:\\NARUTO\\contacts.txt"
    app = QApplication(sys.argv)
    contact_window = ContactWindow(contacts_path)
    contact_window.show()
    sys.exit(app.exec_())
