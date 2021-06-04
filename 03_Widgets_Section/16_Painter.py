from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("PyQt5 Drawing")
        self.setWindowIcon(QIcon("python.png"))

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        # painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))
        painter.drawRect(100, 15, 100, 100)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())