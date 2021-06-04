import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Loading the ui file with uic module
        uic.loadUi("14_Slider.ui", self)
        # finding the widget

        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.change_slider)

        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)

        self.label = self.findChild(QLabel, "label")

    def change_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))


if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    sys.exit(app.exec_())