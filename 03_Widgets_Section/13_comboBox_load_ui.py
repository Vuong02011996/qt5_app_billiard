from PyQt5.QtWidgets import QApplication,\
    QWidget, QComboBox, QLabel
from PyQt5 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi('13_ComboBox.ui', self)

        #find widgets in the ui file
        self.combo = self.findChild(QComboBox, "comboBox")
        self.combo.currentTextChanged.connect(self.combo_selected)
        self.label = self.findChild(QLabel, "label")

    def combo_selected(self):
        item = self.combo.currentText()
        self.label.setText("You selected : " + item)


app = QApplication([])
window = UI()
window.show()
app.exec_()