# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'negahbani.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1121, 791))
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(590, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(520, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(790, 200, 151, 22))
        self.lineEdit_3.setCursorPosition(0)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(910, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(1030, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(790, 320, 151, 22))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "افسر جانشین")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 240, 151, 22))
        self.lineEdit_4.setCursorPosition(0)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(910, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(790, 80, 151, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(910, 320, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 160, 151, 22))
        self.lineEdit_6.setCursorPosition(0)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(910, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(790, 120, 151, 22))
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(920, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(790, 280, 151, 22))
        self.lineEdit_5.setCursorPosition(0)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(910, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tableAfrad = QtWidgets.QTableView(self.tab)
        self.tableAfrad.setGeometry(QtCore.QRect(50, 370, 1021, 351))
        self.tableAfrad.setObjectName("tableAfrad")
        self.refreshbtn = QtWidgets.QPushButton(self.tab)
        self.refreshbtn.setGeometry(QtCore.QRect(590, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refreshbtn.setFont(font)
        self.refreshbtn.setObjectName("refreshbtn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(940, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(770, 40, 151, 22))
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(940, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(770, 130, 261, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(770, 80, 151, 22))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(30, 170, 1001, 571))
        self.tableView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableView.setObjectName("tableView")
        self.searchbtn = QtWidgets.QPushButton(self.tab_2)
        self.searchbtn.setGeometry(QtCore.QRect(560, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.searchbtn.setFont(font)
        self.searchbtn.setObjectName("searchbtn")
        self.printbtn = QtWidgets.QPushButton(self.tab_2)
        self.printbtn.setGeometry(QtCore.QRect(360, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.printbtn.setFont(font)
        self.printbtn.setObjectName("printbtn")
        self.copybtn = QtWidgets.QPushButton(self.tab_2)
        self.copybtn.setGeometry(QtCore.QRect(160, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.copybtn.setFont(font)
        self.copybtn.setObjectName("copybtn")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(self.label.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "main"))
        self.pushButton.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_2.setText(_translate("MainWindow", "ویرایش"))
        self.pushButton_3.setText(_translate("MainWindow", "حذف"))
        self.pushButton_4.setText(_translate("MainWindow", "جستجو"))
        self.label.setText(_translate("MainWindow", "مدیریت پرسنل"))
        self.label_7.setText(_translate("MainWindow", "کد پرسنلی"))
        self.label_2.setText(_translate("MainWindow", "نام"))
        self.comboBox.setItemText(1, _translate("MainWindow", "افسرنگهبان"))
        self.comboBox.setItemText(2, _translate("MainWindow", "معاون افسر نگهبان"))
        self.comboBox.setItemText(3, _translate("MainWindow", "رئیس پاسدار"))
        self.label_3.setText(_translate("MainWindow", "کد ملی"))
        self.label_5.setText(_translate("MainWindow", "بخش شیفت"))
        self.label_4.setText(_translate("MainWindow", "درجه نظامی"))
        self.label_6.setText(_translate("MainWindow", "تعداد شیفت در ماه"))
        self.label_9.setText(_translate("MainWindow", "نام خانوادگی"))
        self.refreshbtn.setText(_translate("MainWindow", "بروزرسانی"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "پرسنل"))
        self.label_8.setText(_translate("MainWindow", "سال"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1400"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1401"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1402"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1403"))
        self.label_10.setText(_translate("MainWindow", "ماه"))
        self.pushButton_7.setText(_translate("MainWindow", "تولید لوحه نگهبانی "))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "فروردین"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "اردیبهشت"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "خرداد"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "تیر"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "مرداد"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "شهریور"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "مهر"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "آبان"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "آذر"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "دی"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "بهمن"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "اسفند"))
        self.searchbtn.setText(_translate("MainWindow", "جستجو و نمایش"))
        self.printbtn.setText(_translate("MainWindow", "چاپ لوحه"))
        self.copybtn.setText(_translate("MainWindow", "کپی از جدول"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "نگهبانی"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
