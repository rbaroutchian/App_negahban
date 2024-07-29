import sys
import sqlite3
import calendar
import datetime
from PyQt5.QtCore import Qt, QRectF, QPoint, QDate, QSize
from PyQt5.QtGui import QPainter, QTextDocument, QFont, QPageLayout, QPageSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QVBoxLayout, QMessageBox, QDialog, QLineEdit , QComboBox, QPushButton, QFileDialog, QTableView, QVBoxLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from negahbani import Ui_MainWindow
import random
from PyQt5 import uic

from fpdf import FPDF

from persiantools.jdatetime import JalaliDate, JalaliDateTime  
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch

import pandas as pd
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from docx import Document
from docx.shared import Inches
from docx.oxml.ns import qn







from negahbani import Ui_MainWindow  

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initDatabase()
        self.initUI()
        self.populateTable()
        self.pushButton.clicked.connect(self.saveData)
        self.pushButton_3.clicked.connect(self.deleteData)
        self.pushButton_2.clicked.connect(self.editData)
        self.pushButton_4.clicked.connect(self.searchData)
        self.refreshbtn.clicked.connect(self.refreshData)
        self.pushButton_7.clicked.connect(self.createShiftTable)
        self.copybtn.clicked.connect(self.copy_to_clipboard)
        self.printbtn.clicked.connect(self.generate_pdf)
        self.searchbtn.clicked.connect(self.loadShiftsFromDatabase)
        self.tabWidget.setCurrentIndex(0)  # تغییر شاخص به 0 برای نمایش تب اول

        
        
        # Dummy data for the shift model
        self.shiftModel = QStandardItemModel(30, 6)  # Example for a month with 30 days
        self.shiftModel.setHorizontalHeaderLabels(['روز', 'تاریخ', 'افسر جانشین', 'افسر نگهبان', 'معاون افسر نگهبان', 'رییس پاسدار'])
        self.tableView.setModel(self.shiftModel)





        self.editing_kodperseneli = None  # متغیر برای ذخیره کد پرسنلی در حالت ویرایش
        
        # دیکشنری ها
        self.month_dict = {
            'فروردین': 1, 'اردیبهشت': 2, 'خرداد': 3, 'تیر': 4,
            'مرداد': 5, 'شهریور': 6, 'مهر': 7, 'آبان': 8,
            'آذر': 9, 'دی': 10, 'بهمن': 11, 'اسفند': 12
        }

        self.year_dict = {
            '1400': 1400, '1401': 1401, '1402': 1402, '1403': 1403,
            '1404': 1404, '1405': 1405, '1406': 1406, '1407': 1407,
            '1408': 1408, '1409': 1409, '1410': 1410  # و ادامه...
        }
        
        
        

    
    def initDatabase(self):
        self.conn = sqlite3.connect('negahbani.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                kodperseneli INTEGER NOT NULL,
                kodmeli INTEGER NOT NULL,
                darje TEXT NOT NULL,
                tedadshift TEXT NOT NULL,
                bakhsh TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS shifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER NOT NULL,
                month INTEGER NOT NULL,
                day INTEGER NOT NULL,
                day_of_week TEXT NOT NULL,
                afsar_janshin TEXT,
                afsar_negaahban TEXT,
                moavin_afsar_negaahban TEXT,
                rayis_pasdar TEXT
            )
        ''')
        
        

        self.conn.commit()
        
    def initUI(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['نام', 'نام خانوادگی', 'کد پرسنلی', 'کد ملی', 'درجه نظامی', 'تعداد شیفت درماه', 'بخش شیفت'])
        self.tableAfrad.setModel(self.model)    
        
        
        # self.tableView.setModel(QStandardItemModel())
        
        self.shiftModel = QStandardItemModel()
        self.shiftModel.setHorizontalHeaderLabels(['روز', 'تاریخ', 'افسر جانشین', 'افسر نگهبان', 'معاون افسر نگهبان', 'رییس پاسدار'])
        self.tableView.setModel(self.shiftModel)

        
        
        
    def saveData(self):
        # جمع‌آوری داده‌ها از فیلدهای ورودی
        name = self.lineEdit.text()
        lastname = self.lineEdit_2.text()
        kodperseneli = self.lineEdit_6.text()
        kodmeli = self.lineEdit_3.text()
        darje = self.lineEdit_4.text()
        tedadshift = self.lineEdit_5.text()
        bakhsh = self.comboBox.currentText()
        
        if name and lastname and kodperseneli and kodmeli and darje and tedadshift and bakhsh:
            try:
                if self.editing_kodperseneli is None:
                    # ذخیره داده‌ها در دیتابیس
                    self.cursor.execute('''
                        INSERT INTO person (name, lastname, kodperseneli, kodmeli, darje, tedadshift, bakhsh) VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (name, lastname, kodperseneli, kodmeli, darje, tedadshift, bakhsh))
                else:
                    # بروزرسانی داده‌ها در دیتابیس
                    self.cursor.execute('''
                        UPDATE person
                        SET name = ?, lastname = ?, kodmeli = ?, darje = ?, tedadshift = ?, bakhsh = ?
                        WHERE kodperseneli = ?
                    ''', (name, lastname, kodmeli, darje, tedadshift, bakhsh, self.editing_kodperseneli))
                    self.editing_kodperseneli = None  # ریست کردن حالت ویرایش
                self.conn.commit()
                QMessageBox.information(self, "Success", "Data saved successfully!")
                self.populateTable()  # بروزرسانی جدول پس از ذخیره داده
                # self.resetFields()
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save data: {e}")
        else:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields")
            
    def resetFields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.comboBox.setCurrentIndex(0)
        
    def deleteData(self):
        selected_indexes = self.tableAfrad.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            kodperseneli_to_delete = self.model.item(row, 2).text().strip()  # گرفتن کد پرسنلی از ردیف انتخاب شده
            # id_to_delete = self.model.item(row, 0).text()  # دریافت آی دی ردیف انتخاب شده
            reply = QMessageBox.question(self, 'Delete Confirmation', f'آیا از حذف  این فرد با کد پرسنلی  {kodperseneli_to_delete} مطمئن هستید ?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.cursor.execute('DELETE FROM person WHERE kodperseneli = ?', (kodperseneli_to_delete,))
                    self.conn.commit()

                    if self.cursor.rowcount > 0:

                        QMessageBox.information(self, "موفقیت آمیز", "ردیف انتخابی حذف شد!")
                        self.refreshData()  # بروزرسانی جدول پس از حذف داده
                except Exception as e:
                    QMessageBox.critical(self, "خطا", f"خطا در هنگام حذف رکورد: {e}")
                    
        else:
            QMessageBox.warning(self, "خطای انتخاب", "لطفا ردیف مورد نظر را انتخب کنید.")
            
    def editData(self):
        selected_indexes = self.tableAfrad.selectedIndexes()
        if selected_indexes:
            self.selected_row = selected_indexes[0].row()
            self.editing_kodperseneli = self.model.item(self.selected_row, 2).text()  # استفاده از کد پرسنلی برای شناسایی رکورد

            name = self.model.item(self.selected_row, 0).text()
            lastname = self.model.item(self.selected_row, 1).text()
            kodperseneli = self.model.item(self.selected_row, 2).text()
            kodmeli = self.model.item(self.selected_row, 3).text()
            darje = self.model.item(self.selected_row, 4).text()
            tedadshift = self.model.item(self.selected_row, 5).text()
            bakhsh = self.model.item(self.selected_row, 6).text()
            
            self.lineEdit.setText(name)
            self.lineEdit_2.setText(lastname)
            self.lineEdit_6.setText(kodperseneli)
            self.lineEdit_3.setText(kodmeli)
            self.lineEdit_4.setText(darje)
            self.lineEdit_5.setText(tedadshift)
            self.comboBox.setCurrentText(bakhsh)
            
            self.editing_kodperseneli = kodperseneli

        else:
            QMessageBox.warning(self, "Selection Error", "Please select a row to edit.")
            
   
    def populateTable(self):
        self.model.removeRows(0, self.model.rowCount())  
        self.cursor.execute("SELECT name, lastname, kodperseneli, kodmeli, darje, tedadshift, bakhsh FROM person")
        data = self.cursor.fetchall()
        
        # Insert rows into the model
        for row_data in data:
            items = [QStandardItem(str(field)) for field in row_data]
            for item in items:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # غیرفعال کردن ویرایش برای هر آیتم
            self.model.appendRow(items)
            
            
    def searchData(self):
        name = self.lineEdit.text()
        lastname = self.lineEdit_2.text()
        kodperseneli = self.lineEdit_6.text()
        kodmeli = self.lineEdit_3.text()
        darje = self.lineEdit_4.text()
        tedadshift = self.lineEdit_5.text()
        bakhsh = self.comboBox.currentText()

        query = "SELECT name, lastname, kodperseneli, kodmeli, darje, tedadshift, bakhsh FROM person WHERE 1=1"
        params = []
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name.strip()}%")
        if lastname:
            query += " AND lastname LIKE ?"
            params.append(f"%{lastname.strip()}%")
        if kodperseneli:
            query += " AND kodperseneli = ?"
            params.append(kodperseneli.strip())
        if kodmeli:
            query += " AND kodmeli = ?"
            params.append(kodmeli.strip())
        if darje:
            query += " AND darje LIKE ?"
            params.append(f"%{darje.strip()}%")
        if tedadshift:
            query += " AND tedadshift LIKE ?"
            params.append(f"%{tedadshift.strip()}%")
        # if bakhsh:
        #     query += " AND bakhsh LIKE ?"
        #     params.append(f"%{bakhsh.strip()}%")
            
        print("Query:", query)  # چاپ کوئری
        print("Params:", params)  # چاپ پارامترها
        
        
        try:
            self.cursor.execute(query, params)
            data = self.cursor.fetchall()
        except Exception as e:
            print("Database query error:", e)
            QMessageBox.warning(self, "Database Error", "An error occurred while executing the query.")
            return

        
        self.model.removeRows(0, self.model.rowCount())  # خالی کردن مدل قبل از پر کردن
        
        # Insert rows into the model and highlight matching rows
        for row_data in data:
            items = [QStandardItem(str(field)) for field in row_data]
            for item in items:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # غیرفعال کردن ویرایش برای هر آیتم
            self.model.appendRow(items)
        
        if data:
            first_index = self.model.index(0, 0)
            self.tableAfrad.scrollTo(first_index, self.tableAfrad.PositionAtTop)
            self.tableAfrad.selectRow(0)
            
    def refreshData(self):
        self.populateTable()
        self.resetFields()
        
    def createShiftTable(self):
    # دریافت مقادیر ورودی از کمبوباکس‌ها
        month_name = self.comboBox_3.currentText()
        year_name = self.comboBox_2.currentText()

    # تبدیل نام ماه و سال به مقادیر عددی
        month = self.month_dict.get(month_name)
        year = self.year_dict.get(year_name)
  
        if month is None or year is None:
            QMessageBox.warning(self, "Input Error", "Please select valid year and month.")
            return

    # دریافت داده‌های جدول قبلی
        self.cursor.execute("SELECT name, lastname, kodperseneli, bakhsh, tedadshift FROM person")
        data = self.cursor.fetchall()
 
    # تعداد روزهای ماه
        if month < 12:
           num_days = (JalaliDateTime(year, month + 1, 1) - JalaliDateTime(year, month, 1)).days
        else:
           num_days = (JalaliDateTime(year + 1, 1, 1) - JalaliDateTime(year, month, 1)).days        


     # تنظیم مدل جدید برای جدول
        self.shiftModel = QStandardItemModel(num_days, 6)
        headers = ['روز', 'تاریخ', 'افسر جانشین', 'افسرنگهبان', 'معاون افسر نگهبان', 'رئیس پاسدار']
        self.shiftModel.setHorizontalHeaderLabels(headers)
        
        
       

    # تعیین روزهای هفته با توجه به تاریخ
        days_of_week = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه']
          # دسته‌بندی افراد بر اساس بخش
        people_by_bakhsh = {header: [] for header in headers[2:]}

        for person in data:
            if len(person) == 5:  # اطمینان از تعداد مقادیر
                name, lastname, kodperseneli, bakhsh, tedadshift = person
                if bakhsh in people_by_bakhsh:
                    people_by_bakhsh[bakhsh].append({'name': name, 'lastname': lastname, 'remaining_shifts': int(tedadshift)})
                else:
                    print(f"Warning: Unknown section '{bakhsh}' for person {name} {lastname}")
                    
                    
                    
        for section, people in people_by_bakhsh.items():
            print(f"Section: {section}")
            for person in people:
                print(f"  {person['name']} {person['lastname']} - Remaining Shifts: {person['remaining_shifts']}")


            
       

        # پر کردن جدول با روزها و تاریخ‌ها
        for day in range(1, num_days + 1):
            persian_date = JalaliDate(year, month, day).strftime('%Y/%m/%d')
            weekday = JalaliDate(year, month, day).weekday()
            day_of_week = days_of_week[weekday]

            self.shiftModel.setItem(day - 1, 0, QStandardItem(day_of_week))
            self.shiftModel.setItem(day - 1, 1, QStandardItem(persian_date))

    # تخصیص شیفت‌ها به روزها
        for section in headers[2:]:
            available_people = people_by_bakhsh[section]
            days_available = list(range(num_days))  # لیست روزهای قابل استفاده

            for person in available_people:
                name = person['name']
                lastname = person['lastname']
                remaining_shifts = person['remaining_shifts']

                if remaining_shifts == 0:
                   continue

            # انتخاب تصادفی روزها برای تخصیص شیفت
                selected_days = random.sample(days_available, min(remaining_shifts, len(days_available)))
                
                print(f"Assigning shifts for {name} {lastname} to days {selected_days}")


                for day in selected_days:
                    self.shiftModel.setItem(day, headers.index(section), QStandardItem(f"{name} {lastname}"))
                    days_available.remove(day)  # حذف روز از لیست قابل استفاده
                    remaining_shifts -= 1

                    if remaining_shifts == 0:
                       break

            # بروزرسانی تعداد شیفت‌های باقی‌مانده
                person['remaining_shifts'] = remaining_shifts

    # ثبت شیفت‌های روز جاری در پایگاه داده
        for day in range(num_days):
            self.cursor.execute('''
                INSERT INTO shifts (year, month, day, day_of_week, afsar_janshin, afsar_negaahban, moavin_afsar_negaahban, rayis_pasdar) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (year, month, day + 1, 
                  self.shiftModel.item(day, 0).text() if self.shiftModel.item(day, 0) else "", 
                  self.shiftModel.item(day, headers.index('افسر جانشین')).text() if self.shiftModel.item(day, headers.index('افسر جانشین')) else "",
                  self.shiftModel.item(day, headers.index('افسرنگهبان')).text() if self.shiftModel.item(day, headers.index('افسرنگهبان')) else "",
                  self.shiftModel.item(day, headers.index('معاون افسر نگهبان')).text() if self.shiftModel.item(day, headers.index('معاون افسر نگهبان')) else "",
                  self.shiftModel.item(day, headers.index('رئیس پاسدار')).text() if self.shiftModel.item(day, headers.index('رئیس پاسدار')) else ""))

        
                    
        self.conn.commit()
        self.refreshData()
    # اتصال مدل به QTableView
        self.tableView.setModel(self.shiftModel)
        
        
        
        
    def loadShiftsFromDatabase(self):
        month_name = self.comboBox_3.currentText()
        year_name = self.comboBox_2.currentText()

       # تبدیل نام ماه و سال به مقادیر عددی
        month = self.month_dict.get(month_name)
        year = self.year_dict.get(year_name)

        if month is None or year is None:
            QMessageBox.warning(self, "Input Error", "Please select valid year and month.")
            return

    # دریافت داده‌های شیفت از پایگاه داده
        self.cursor.execute('''
            SELECT day, day_of_week, afsar_janshin, afsar_negaahban, moavin_afsar_negaahban, rayis_pasdar 
            FROM shifts WHERE year = ? AND month = ?
        ''', (year, month))

        shifts = self.cursor.fetchall()
    
        if not shifts:
            QMessageBox.information(self, "No Data", "No shift data found for the selected month and year.")
            return

    # تنظیم مدل جدید برای جدول
        self.shiftModel = QStandardItemModel(len(shifts), 6)
        headers = ['روز', 'تاریخ', 'افسر جانشین', 'افسر نگهبان', 'معاون افسر نگهبان', 'رییس پاسدار']
        self.shiftModel.setHorizontalHeaderLabels(headers)

    # پر کردن جدول با داده‌های بازیابی شده
        for row, shift in enumerate(shifts):
            day, day_of_week, afsar_janshin, afsar_negaahban, moavin_afsar_negaahban, rayis_pasdar = shift
            persian_date = JalaliDate(year, month, day).strftime('%Y/%m/%d')

            self.shiftModel.setItem(row, 0, QStandardItem(day_of_week))
            self.shiftModel.setItem(row, 1, QStandardItem(persian_date))
            self.shiftModel.setItem(row, 2, QStandardItem(afsar_janshin))
            self.shiftModel.setItem(row, 3, QStandardItem(afsar_negaahban))
            self.shiftModel.setItem(row, 4, QStandardItem(moavin_afsar_negaahban))
            self.shiftModel.setItem(row, 5, QStandardItem(rayis_pasdar))

    # اتصال مدل به QTableView
        self.tableView.setModel(self.shiftModel)
    
    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        data = []

        # افزودن سرستون‌ها
        header = []
        for col in range(self.shiftModel.columnCount()):
            header_item = self.shiftModel.horizontalHeaderItem(col)
            if header_item:
                header.append(header_item.text())
            else:
                header.append("")
        data.append("\t".join(header))

        # افزودن داده‌های جدول
        for row in range(self.shiftModel.rowCount()):
            row_data = []
            for col in range(self.shiftModel.columnCount()):
                item = self.shiftModel.item(row, col)
                if item:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append("\t".join(row_data))

        clipboard.setText("\n".join(data))  # کپی به کلیپ‌بورد به فرمت tab-separated
        QMessageBox.information(self, "Copied", "Shift table has been copied to clipboard!")
        
    def generate_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)")
        if not filename:
            return

        doc = SimpleDocTemplate(filename, pagesize=letter)
        content = []

        pdfmetrics.registerFont(TTFont('Tahoma', 'font/Tahoma.ttf'))

        styles = getSampleStyleSheet()
        title_style = styles['Title']
        title_style.fontName = 'Tahoma'
        
        
        content.append(Paragraph("Shift Table Report", title_style))

        data = [['روز', 'تاریخ', 'افسر جانشین', 'افسر نگهبان', 'معاون افسر نگهبان', 'رییس پاسدار']]
        for row in range(self.shiftModel.rowCount()):
            row_data = []
            for col in range(self.shiftModel.columnCount()):
                item = self.shiftModel.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Tahoma'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        content.append(table)

        doc.build(content)
        QMessageBox.information(self, "PDF Generated", "PDF has been generated successfully!")


        


    
    
    
    def closeEvent(self, event):
        self.conn.close()
        event.accept()
        

        
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("فرم ورود")
        
        # Create widgets
        self.username_label = QLabel("نام کاربری:")
        self.password_label = QLabel("رمز عبور:")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("ورود")
        self.cancel_button = QPushButton("خروج")

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        # Connect buttons
        self.login_button.clicked.connect(self.check_login)
        self.cancel_button.clicked.connect(self.reject)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace this with your actual authentication logic
        if username == "admin" and password == "admin":
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Show login window first
    login = LoginWindow()
    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()  # Exit application if login fails