import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QApplication
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Loading the ui file with uic module
        uic.loadUi("15_Menu.ui", self)


if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    sys.exit(app.exec_())