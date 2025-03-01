import sys
from PySide6.QtWidgets import QApplication, QWidget
from visionmainfile import Ui_NARUTOAIUI

class NARUTOAIUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NARUTOAIUI()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NARUTOAIUI()
    widget.show()
    sys.exit(app.exec())
