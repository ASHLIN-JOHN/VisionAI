# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form import Ui_loginWindowClass

class loginWindowClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_loginWindowClass()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = loginWindowClass()
    widget.show()
    sys.exit(app.exec())
