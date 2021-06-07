from PyQt5.QtWidgets import QApplication,\
    QWidget, QComboBox, QLabel, QLCDNumber,\
    QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QSpinBox, QCheckBox, QTabWidget, \
    QToolButton, QStyle, QGridLayout, QMessageBox

from PyQt5 import QtCore
from PyQt5 import uic
from datetime import datetime, timezone, timedelta

# Form = QWidget()


def convert_time_to_epoch(s):
    today = datetime.today()  # 2020-09-16
    # make a datetime object with today's date
    dt = datetime.combine(today, datetime.strptime(s, '%H:%M:%S').time())
    # make sure it's in UTC (optional)
    dt = dt.replace(tzinfo=timezone.utc)
    # get the timestamp
    ts = dt.timestamp()
    return ts


class TabPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # loading the ui file with uic module

        uic.loadUi('bida1.ui', self)

        """===============================TIEN BAN======================================"""
        self.lcd_gio = self.findChild(QLCDNumber, "lcd_gio")

        self.label_tg_bat_dau = self.findChild(QLabel, "label_tg_bat_dau")
        self.label_tg_dung = self.findChild(QLabel, "label_tg_dung")
        self.label_tong_tg = self.findChild(QLabel, "label_tong_tg")
        self.label_thanh_tien_gio = self.findChild(QLabel, "label_thanh_tien_gio")

        self.pushButton_bdtg = self.findChild(QPushButton, "pushButton_bdtg")
        self.pushButton_bdtg.clicked.connect(self.clicked_bdtg)

        self.pushButton_dung = self.findChild(QPushButton, "pushButton_dung")
        self.pushButton_dung.clicked.connect(self.clicked_dung)
        self.lineEdit_tien_mot_gio = self.findChild(QLineEdit, "lineEdit_tien_mot_gio")

        self.pushButton_xoa = self.findChild(QPushButton, "pushButton_xoa")
        self.pushButton_xoa.clicked.connect(self.clicked_xoa)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
        """==========================THUC DON =================================================="""

        # Gia mon an
        self.lineEdit_gia_mi_tom = self.findChild(QLineEdit, "lineEdit_gia_mi_tom")
        self.lineEdit_gia_nuti = self.findChild(QLineEdit, "lineEdit_gia_nuti")
        self.lineEdit_gia_nha_dam = self.findChild(QLineEdit, "lineEdit_gia_nha_dam")
        self.lineEdit_gia_heniken = self.findChild(QLineEdit, "lineEdit_gia_heniken")
        self.lineEdit_gia_tiger = self.findChild(QLineEdit, "lineEdit_gia_tiger")
        self.lineEdit_gia_bo_huc = self.findChild(QLineEdit, "lineEdit_gia_bo_huc")
        self.lineEdit_gia_coca = self.findChild(QLineEdit, "lineEdit_gia_coca")
        self.lineEdit_gia_tra_0_do = self.findChild(QLineEdit, "lineEdit_gia_tra_0_do")
        self.lineEdit_gia_sting = self.findChild(QLineEdit, "lineEdit_gia_sting")
        self.lineEdit_gia_tra_o_long = self.findChild(QLineEdit, "lineEdit_gia_tra_o_long")

        # thanh tien
        self.label_tien_mi_tom = self.findChild(QLabel, "label_tien_mi_tom")
        self.label_tien_nuti = self.findChild(QLabel, "label_tien_nuti")
        self.label_tien_nha_dam = self.findChild(QLabel, "label_tien_nha_dam")
        self.label_tien_heniken = self.findChild(QLabel, "label_tien_heniken")
        self.label_tien_tiger = self.findChild(QLabel, "label_tien_tiger")
        self.label_tien_bo_huc = self.findChild(QLabel, "label_tien_bo_huc")
        self.label_tien_coca = self.findChild(QLabel, "label_tien_coca")
        self.label_tien_tra_0_do = self.findChild(QLabel, "label_tien_tra_0_do")
        self.label_tien_sting = self.findChild(QLabel, "label_tien_sting")
        self.label_tien_tra_o_long = self.findChild(QLabel, "label_tien_tra_o_long")

        self.label_tong_tien_thuc_don = self.findChild(QLabel, "label_tong_tien_thuc_don")

        # so luong
        self.spinBox_sl_mi_tom = self.findChild(QSpinBox, "spinBox_sl_mi_tom")
        self.spinBox_sl_nuti = self.findChild(QSpinBox, "spinBox_sl_nuti")
        self.spinBox_sl_nha_dam = self.findChild(QSpinBox, "spinBox_sl_nha_dam")
        self.spinBox_sl_heniken = self.findChild(QSpinBox, "spinBox_sl_heniken")
        self.spinBox_sl_tiger = self.findChild(QSpinBox, "spinBox_sl_tiger")
        self.spinBox_sl_bo_huc = self.findChild(QSpinBox, "spinBox_sl_bo_huc")
        self.spinBox_sl_coca = self.findChild(QSpinBox, "spinBox_sl_coca")
        self.spinBox_sl_tra_0_do = self.findChild(QSpinBox, "spinBox_sl_tra_0_do")
        self.spinBox_sl_nuoc_sting = self.findChild(QSpinBox, "spinBox_sl_nuoc_sting")
        self.spinBox_sl_tra_o_long = self.findChild(QSpinBox, "spinBox_sl_tra_o_long")

        # check box mon an
        self.checkBox_mi_tom = self.findChild(QCheckBox, "checkBox_mi_tom")
        self.checkBox_sua_nuti = self.findChild(QCheckBox, "checkBox_sua_nuti")
        self.checkBox_nha_dam = self.findChild(QCheckBox, "checkBox_nha_dam")
        self.checkBox_heniken = self.findChild(QCheckBox, "checkBox_heniken")
        self.checkBox_tiger = self.findChild(QCheckBox, "checkBox_tiger")
        self.checkBox_bo_huc = self.findChild(QCheckBox, "checkBox_bo_huc")
        self.checkBox_coca = self.findChild(QCheckBox, "checkBox_coca")
        self.checkBox_tra_0_do = self.findChild(QCheckBox, "checkBox_tra_0_do")
        self.checkBox_sting = self.findChild(QCheckBox, "checkBox_sting")
        self.checkBox_tra_o_long = self.findChild(QCheckBox, "checkBox_tra_o_long")

        # change so luong
        self.spinBox_sl_mi_tom.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_mi_tom,
                                                                               self.spinBox_sl_mi_tom,
                                                                               self.label_tien_mi_tom,
                                                                               self.checkBox_mi_tom))
        self.spinBox_sl_nuti.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_nuti,
                                                                             self.spinBox_sl_nuti,
                                                                             self.label_tien_nuti,
                                                                             self.checkBox_sua_nuti))
        self.spinBox_sl_nha_dam.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_nha_dam,
                                                                                self.spinBox_sl_nha_dam,
                                                                                self.label_tien_nha_dam,
                                                                                self.checkBox_nha_dam))
        self.spinBox_sl_heniken.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_heniken,
                                                                                self.spinBox_sl_heniken,
                                                                                self.label_tien_heniken,
                                                                                self.checkBox_heniken))
        self.spinBox_sl_tiger.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_tiger,
                                                                              self.spinBox_sl_tiger,
                                                                              self.label_tien_tiger,
                                                                              self.checkBox_tiger))
        self.spinBox_sl_bo_huc.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_bo_huc,
                                                                              self.spinBox_sl_bo_huc,
                                                                              self.label_tien_bo_huc,
                                                                              self.checkBox_bo_huc))
        self.spinBox_sl_coca.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_coca,
                                                                              self.spinBox_sl_coca,
                                                                              self.label_tien_coca,
                                                                              self.checkBox_coca))
        self.spinBox_sl_tra_0_do.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_tra_0_do,
                                                                              self.spinBox_sl_tra_0_do,
                                                                              self.label_tien_tra_0_do,
                                                                              self.checkBox_tra_0_do))
        self.spinBox_sl_nuoc_sting.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_sting,
                                                                              self.spinBox_sl_nuoc_sting,
                                                                              self.label_tien_sting,
                                                                              self.checkBox_sting))
        self.spinBox_sl_tra_o_long.valueChanged.connect(lambda: self.spin_selected(self.lineEdit_gia_tra_o_long,
                                                                              self.spinBox_sl_tra_o_long,
                                                                              self.label_tien_tra_o_long,
                                                                              self.checkBox_tra_o_long))

        # chon mon an
        self.checkBox_mi_tom.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_mi_tom,
                                                                              self.lineEdit_gia_mi_tom,
                                                                              self.spinBox_sl_mi_tom,
                                                                              self.label_tien_mi_tom))
        self.checkBox_sua_nuti.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_sua_nuti,
                                                                                self.lineEdit_gia_nuti,
                                                                                self.spinBox_sl_nuti,
                                                                                self.label_tien_nuti))
        self.checkBox_nha_dam.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_nha_dam,
                                                                               self.lineEdit_gia_nha_dam,
                                                                               self.spinBox_sl_nha_dam,
                                                                               self.label_tien_nha_dam))
        self.checkBox_heniken.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_heniken,
                                                                               self.lineEdit_gia_heniken,
                                                                               self.spinBox_sl_heniken,
                                                                               self.label_tien_heniken))
        self.checkBox_tiger.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_tiger,
                                                                             self.lineEdit_gia_tiger,
                                                                             self.spinBox_sl_tiger,
                                                                             self.label_tien_tiger))
        self.checkBox_bo_huc.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_bo_huc,
                                                                             self.lineEdit_gia_bo_huc,
                                                                             self.spinBox_sl_bo_huc,
                                                                             self.label_tien_bo_huc))
        self.checkBox_coca.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_coca,
                                                                             self.lineEdit_gia_coca,
                                                                             self.spinBox_sl_coca,
                                                                             self.label_tien_coca))
        self.checkBox_tra_0_do.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_tra_0_do,
                                                                             self.lineEdit_gia_tra_0_do,
                                                                             self.spinBox_sl_tra_0_do,
                                                                             self.label_tien_tra_0_do))
        self.checkBox_sting.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_sting,
                                                                             self.lineEdit_gia_sting,
                                                                             self.spinBox_sl_nuoc_sting,
                                                                             self.label_tien_sting))
        self.checkBox_tra_o_long.stateChanged.connect(lambda: self.checked_mon_an(self.checkBox_tra_o_long,
                                                                             self.lineEdit_gia_tra_o_long,
                                                                             self.spinBox_sl_tra_o_long,
                                                                             self.label_tien_tra_o_long))

        self.pushButton_xoa_don = self.findChild(QPushButton, "pushButton_xoa_don")
        self.pushButton_xoa_don.clicked.connect(self.xoa_don)

        # Tinh tong
        self.label_tien_thuc_don_tinh_tong = self.findChild(QLabel, "label_tien_thuc_don_tinh_tong")
        self.label_tien_ban_tinh_tong = self.findChild(QLabel, "label_tien_ban_tinh_tong")
        self.label_tong_tien_khach = self.findChild(QLabel, "label_tong_tien_khach")
        self.pushButton_tong_tien = self.findChild(QPushButton, "pushButton_tong_tien")
        self.pushButton_tong_tien.clicked.connect(self.tinh_tong_tien)

        # Thoi lai
        self.pushButton_thoi_lai = self.findChild(QPushButton, "pushButton_thoi_lai")
        self.pushButton_thoi_lai.clicked.connect(self.thoi_lai)
        self.lineEdit_khach_dua = self.findChild(QLineEdit, "lineEdit_khach_dua")
        self.label_tien_thoi_lai = self.findChild(QLabel, "label_tien_thoi_lai")


    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.lcd_gio.display(text)

    def clicked_bdtg(self):
        if self.label_tg_bat_dau.text() != "00:00:00":
            message = QMessageBox.question(self, "Choice Message",
                                           "Thời gian bắt đầu khác 0!Bạn có muốn bắt đầu lại?",
                                           QMessageBox.Yes | QMessageBox.No)

            if message == QMessageBox.Yes:
                time = QtCore.QTime.currentTime()
                text = time.toString('hh:mm:ss')
                # text = text.split(":")
                # text = text[0] + "_giờ_" + text[1] + "_phút"
                self.label_tg_bat_dau.setText(text)
            else:
                self.label_tg_bat_dau.setText(self.label_tg_bat_dau.text())
        else:
            time = QtCore.QTime.currentTime()
            text = time.toString('hh:mm:ss')
            # text = text.split(":")
            # text = text[0] + "_giờ_" + text[1] + "_phút"
            self.label_tg_bat_dau.setText(text)

    def clicked_dung(self):
        tg_bat_dau = self.label_tg_bat_dau.text()
        if tg_bat_dau == "00:00:00":
            print("message chua bat dau")
        else:
            time = QtCore.QTime.currentTime()
            text = time.toString('hh:mm:ss')
            # text = text.split(":")
            # text = text[0] + "_giờ_" + text[1] + "_phút"
            self.label_tg_dung.setText(text)
            tg_dung = self.label_tg_dung.text()
            tg_dung = convert_time_to_epoch(tg_dung)

            tg_bat_dau = convert_time_to_epoch(tg_bat_dau)
            tong_tg = int(tg_dung - tg_bat_dau)
            conversion = timedelta(seconds=tong_tg)
            print(str(conversion))
            tong_tg = str(conversion).split(":")
            text = tong_tg[0] + "_giờ_" + tong_tg[1] + "_phút"
            self.label_tong_tg.setText(text)

            tien_mot_phut = (int(self.lineEdit_tien_mot_gio.text().split("k")[0]) * 1000) / 60
            tien_gio = (int(tong_tg[0]) * 60 + int(tong_tg[1])) * int(tien_mot_phut)
            self.label_thanh_tien_gio.setText(str(tien_gio) + "đ")
            self.label_tien_ban_tinh_tong.setText(str(tien_gio) + "đ")

    def clicked_xoa(self):
        text = "00:00:00"
        self.label_tg_bat_dau.setText(text)
        self.label_tg_dung.setText(text)
        text = "0_giờ_" + "00_phút"
        self.label_tong_tg.setText(text)
        self.label_thanh_tien_gio.setText("0đ")
        self.label_tien_ban_tinh_tong.setText("0đ")

    def spin_selected(self, line_edit_don_gia, spin_box_sl, label_thanh_tien, check_box_mon_an):
        if check_box_mon_an.isChecked():
            so_luong = spin_box_sl.value()
            don_gia = int(line_edit_don_gia.text()[:-1])
            thanh_tien = so_luong * don_gia
            label_thanh_tien.setText(str(thanh_tien) + "đ")
        else:
            label_thanh_tien.setText("0đ")

        tong_tien_thuc_don = self.tinh_tong_tien_thuc_don()
        self.label_tong_tien_thuc_don.setText(str(tong_tien_thuc_don) + "đ")
        self.label_tien_thuc_don_tinh_tong.setText(str(tong_tien_thuc_don) + "đ")

    def checked_mon_an(self, check_box_mon_an, line_edit_don_gia, spin_box_sl, label_thanh_tien):
        if check_box_mon_an.isChecked():
            don_gia = int(line_edit_don_gia.text()[:-1])
            so_luong = spin_box_sl.value()
            thanh_tien = so_luong * don_gia
            label_thanh_tien.setText(str(thanh_tien) + "đ")

            check_box_mon_an.setStyleSheet("QCheckBox\n"
                                           "{\n"
                                           "background-color: rgb(247, 91, 91);\n"
                                           "font: 57 10pt \"Ubuntu\";\n"
                                           "}")

            label_thanh_tien.setStyleSheet("QLabel\n"
                                                "{\n"
                                                "background-color: rgb(247, 91, 91);\n"
                                                "font: 57 10pt \"Ubuntu\";\n"
                                                "}")
            line_edit_don_gia.setStyleSheet("QLineEdit\n"
                                                "{\n"
                                                "background-color: rgb(247, 91, 91);\n"
                                                "font: 57 10pt \"Ubuntu\";\n"
                                                "}")
            spin_box_sl.setStyleSheet("QSpinBox\n"
                                                "{\n"
                                                "background-color: rgb(247, 91, 91);\n"
                                                "font: 57 10pt \"Ubuntu\";\n"
                                                "}")
        else:
            label_thanh_tien.setText("0đ")
            check_box_mon_an.setStyleSheet("QCheckBox\n"
                                           "{\n"
                                           "background-color: rgb(101, 201, 226);\n"
                                           "font: 57 10pt \"Ubuntu\";\n"
                                           "}")

            label_thanh_tien.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "background-color: rgb(101, 201, 226);\n"
                                           "font: 57 10pt \"Ubuntu\";\n"
                                           "}")
            line_edit_don_gia.setStyleSheet("QLineEdit\n"
                                            "{\n"
                                            "background-color: rgb(101, 201, 226);\n"
                                            "font: 57 10pt \"Ubuntu\";\n"
                                            "}")
            spin_box_sl.setStyleSheet("QSpinBox\n"
                                      "{\n"
                                      "background-color: rgb(101, 201, 226);\n"
                                      "font: 57 10pt \"Ubuntu\";\n"
                                      "}")

        tong_tien_thuc_don = self.tinh_tong_tien_thuc_don()
        self.label_tong_tien_thuc_don.setText(str(tong_tien_thuc_don) + "đ")
        self.label_tien_thuc_don_tinh_tong.setText(str(tong_tien_thuc_don) + "đ")

    def tinh_tong_tien_thuc_don(self):
        tong_tien_thuc_don = int(self.label_tien_mi_tom.text()[:-1]) \
                             + int(self.label_tien_nuti.text()[:-1]) \
                             + int(self.label_tien_nha_dam.text()[:-1]) \
                             + int(self.label_tien_heniken.text()[:-1]) \
                             + int(self.label_tien_tiger.text()[:-1]) \
                             + int(self.label_tien_bo_huc.text()[:-1]) \
                             + int(self.label_tien_coca.text()[:-1]) \
                             + int(self.label_tien_tra_0_do.text()[:-1]) \
                             + int(self.label_tien_sting.text()[:-1]) \
                             + int(self.label_tien_tra_o_long.text()[:-1])
        return tong_tien_thuc_don

    def tinh_tong_tien(self):
        tong_tien = int(self.label_tong_tien_thuc_don.text()[:-1]) + int(self.label_tien_ban_tinh_tong.text()[:-1])
        self.label_tong_tien_khach.setText(str(tong_tien) + "đ")

    def thoi_lai(self):
        tien_khach = int(self.lineEdit_khach_dua.text()[:-1])
        tien_thoi_lai = tien_khach - int(self.label_tong_tien_khach.text()[:-1])
        self.label_tien_thoi_lai.setText(str(tien_thoi_lai) + "đ")

    def xoa_don(self):
        self.checkBox_mi_tom.setChecked(False)
        self.checkBox_sua_nuti.setChecked(False)
        self.checkBox_nha_dam.setChecked(False)
        self.checkBox_heniken.setChecked(False)
        self.checkBox_tiger.setChecked(False)
        self.checkBox_bo_huc.setChecked(False)
        self.checkBox_coca.setChecked(False)
        self.checkBox_tra_0_do.setChecked(False)
        self.checkBox_sting.setChecked(False)
        self.checkBox_tra_o_long.setChecked(False)

        self.spinBox_sl_mi_tom.setValue(0)
        self.spinBox_sl_nuti.setValue(0)
        self.spinBox_sl_nha_dam.setValue(0)
        self.spinBox_sl_heniken.setValue(0)
        self.spinBox_sl_tiger.setValue(0)
        self.spinBox_sl_bo_huc.setValue(0)
        self.spinBox_sl_coca.setValue(0)
        self.spinBox_sl_tra_0_do.setValue(0)
        self.spinBox_sl_nuoc_sting.setValue(0)
        self.spinBox_sl_tra_o_long.setValue(0)

        self.label_tien_mi_tom.setText("0đ")
        self.label_tien_nuti.setText("0đ")
        self.label_tien_nha_dam.setText("0đ")
        self.label_tien_heniken.setText("0đ")
        self.label_tien_tiger.setText("0đ")
        self.label_tien_bo_huc.setText("0đ")
        self.label_tien_coca.setText("0đ")
        self.label_tien_tra_0_do.setText("0đ")
        self.label_tien_sting.setText("0đ")
        self.label_tien_tra_o_long.setText("0đ")

        self.label_tong_tien_thuc_don.setText("0đ")
        self.label_tien_thuc_don_tinh_tong.setText("0đ")
        self.label_tien_ban_tinh_tong.setText("0đ")
        self.label_tong_tien_khach.setText("0đ")

        self.label_tien_thoi_lai.setText("0đ")
        self.lineEdit_khach_dua.setText("0đ")


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(124, 244, 145);")
        self.resize(1000, 500)
        self.tabs = QTabWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)
        # https://stackoverflow.com/questions/47556122/button-for-duplicating-tabs-in-a-qtabwidget
        # button = QToolButton()
        # button.setToolTip('Add New Tab')
        # button.clicked.connect(self.addNewTab)
        # button.setIcon(self.style().standardIcon(
        #     QStyle.SP_DialogYesButton))

        button = QPushButton()
        button.setToolTip('Thêm bàn')
        button.clicked.connect(self.addNewTab)
        button.setText("Thêm bàn")
        self.tabs.setCornerWidget(button, QtCore.Qt.TopRightCorner)
        self.addNewTab()

    def addNewTab(self):
        if self.tabs.count() < 5:
            text = 'Bàn %d' % (self.tabs.count() + 1)
            self.tabs.addTab(TabPage(self.tabs), text)
        else:
            print("Khong add them ban duoc")


app = QApplication([])
window = UI()
window.show()
app.exec_()

'''
Them mon
Tinh tien tong , thoi lai
thong ke moi ngay
    + theo tung ban
    + Tong tien h
    + Tong tien thuc an
'''