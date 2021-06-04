from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
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
        vbox = QGridLayout()

        # creating QPushButton
        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")
        btn5 = QPushButton("Click Five")
        btn6 = QPushButton("Click Six")
        btn7 = QPushButton("Click Seven")
        btn8 = QPushButton("Click Eight")

        # Add widgets in the layout
        vbox.addWidget(btn1, 0, 0)
        vbox.addWidget(btn2, 0, 1)
        vbox.addWidget(btn3, 0, 2)
        vbox.addWidget(btn4, 0, 3)
        vbox.addWidget(btn5, 1, 0)
        vbox.addWidget(btn6, 1, 1)
        vbox.addWidget(btn7, 1, 2)
        vbox.addWidget(btn8, 1, 3)

        # set layout for the main window
        self.setLayout(vbox)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())

