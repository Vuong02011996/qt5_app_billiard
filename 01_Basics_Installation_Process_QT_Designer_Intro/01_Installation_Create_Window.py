import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

# Widget la noi tap hop cac tinh nang cua app
# window = QWidget()
# window.show()


class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        # x, y position and width , height window
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Billiard APP")
        self.setWindowIcon(QIcon("../icon.jpeg"))
        self.setStyleSheet("background-color:green")

        self.show()


# Start the event loop
window = WindowExample()
app.exec_()