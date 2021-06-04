from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title , icon and geometry
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("VBoxLayout")
        self.setWindowIcon(QIcon("../icon.jpeg"))

        # vboxlayout object
        vbox = QVBoxLayout()

        # creating QPushButton
        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        # Add widgets in the layout
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        # set layout for the main window
        self.setLayout(vbox)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())

