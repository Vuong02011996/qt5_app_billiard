import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Bida APP")
        self.setWindowIcon(QIcon("../icon.jpeg"))
        self.create_buttons()

    def create_buttons(self):
        btn1 = QPushButton("Click Me", self)
        btn1.setGeometry(100, 100, 100, 100)
        btn1.setIcon(QIcon("../icon.jpeg"))
        btn1.setStyleSheet("color:red")
        btn1.setStyleSheet("background-color:green")

        btn1.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        print("You clicked button")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())


