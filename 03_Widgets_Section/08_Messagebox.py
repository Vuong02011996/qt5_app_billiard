from PyQt5.QtWidgets import QApplication, QWidget,\
    QHBoxLayout, QMessageBox, QPushButton, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200,200,400,200)
        self.setWindowTitle("Creating MessageBox")
        self.setWindowIcon(QIcon("python.png"))

        self.create_messagebox()


    def create_messagebox(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton("Warning")
        btn1.clicked.connect(self.warning_msg)

        btn2 = QPushButton("Information")
        btn2.clicked.connect(self.info_msg)

        btn3 = QPushButton("About")
        btn3.clicked.connect(self.about_msg)

        btn4 = QPushButton("Yes/No")
        btn4.clicked.connect(self.multi_choice_msg)


        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        vbox = QVBoxLayout()

        self.label = QLabel("Text")
        self.label.setFont(QFont("Sanserif", 14))

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)



        self.setLayout(vbox)


    def warning_msg(self):
        QMessageBox.warning(self, "Warning",
                            "This is a warning message")


    def info_msg(self):
        QMessageBox.information(self, "Information",
                                "This is information message")


    def about_msg(self):
        QMessageBox.about(self, "About",
                          "This is about message")



    def multi_choice_msg(self):
        message = QMessageBox.question(self, "Choice Message",
                                       "Do You Like Python ?",
                                       QMessageBox.Yes |
                                       QMessageBox.No)


        if message == QMessageBox.Yes:
            self.label.setText("Yes I Like Python")


        else:
            self.label.setText("No I Dont Like Python")



App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())