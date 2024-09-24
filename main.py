import sys
import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainwindow import Ui_MainWindow
from config import host, user, password, database

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

class Database:
    def __init__(self, connection):
        self.copiedEmployee = []

        self.connection = connection
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True

    def __del__(self):
        self.connection.close()
        self.cursor.close()

database = Database(psycopg2.connect(host=host, user=user, password=password, database=database))

class Interface:
    def __init__(self):
        ui.addBtn.clicked.connect(lambda: self.add_employee())
        ui.deleteBtn.clicked.connect(lambda: self.delete_employee())
        ui.editBtn.clicked.connect(lambda: self.edit_employee())

        ui.personnelTable.verticalHeader().sectionClicked.connect(self.copy_employee)

        self.output_employees()
        self.update_records_number()

    @staticmethod
    def show_message(message):
        msgbox = QMessageBox()
        msgbox.setWindowTitle('Information')
        msgbox.setText(message)
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

        action = msgbox.exec_()

        if action == QMessageBox.Ok:
            return True

    @staticmethod
    def update_records_number():
        query = "SELECT * FROM employees"
        database.cursor.execute(query)
        data = database.cursor.fetchall()
        ui.recordsLabel.setText(f'Total records: {len(data)}')

    def output_employees(self):
        query = """SELECT first_name, surname, patronymic, subdivision, nationality, education, employee_position
                FROM employees"""
        database.cursor.execute(query)
        data = database.cursor.fetchall()
        self.populate_table(ui.personnelTable, data, 7)

    @staticmethod
    def populate_table(table, data, column_count):
        table.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for column_index in range(column_count):
                table.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(row_data[column_index])))

    @staticmethod
    def copy_employee(row):
        items = [ui.personnelTable.item(row, col).text() for col in range(ui.personnelTable.columnCount())]
        database.copiedEmployee = tuple(items)
        text_fields = (ui.firstNameLE, ui.surnameLE, ui.patronymicLE, ui.subdivisionLE,
                       ui.nationalityLE, ui.educationLE, ui.positionLE)
        for i in range(len(text_fields)):
            text_fields[i].setText(items[i])

    @staticmethod
    def get_parameters():
        return (
            ui.firstNameLE.text(),
            ui.surnameLE.text(),
            ui.patronymicLE.text(),
            ui.subdivisionLE.text(),
            ui.nationalityLE.text(),
            ui.educationLE.text(),
            ui.positionLE.text()
        )

    def add_employee(self):
        parameters = self.get_parameters()
        query = """INSERT INTO employees (first_name, surname, patronymic, subdivision, nationality, education, employee_position)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        database.cursor.execute(query, parameters)
        self.output_employees()

    def delete_employee(self):
        res = self.show_message('Are you sure?')
        if res:
            parameters = self.get_parameters()
            query = """DELETE FROM employees
                    WHERE first_name = %s AND surname = %s AND patronymic = %s AND 
                    subdivision = %s AND nationality = %s AND education = %s AND employee_position = %s"""
            database.cursor.execute(query, parameters)
            self.output_employees()

    def edit_employee(self):
        query = """UPDATE employees
                SET first_name = %s, surname = %s, patronymic = %s, 
                subdivision = %s, nationality = %s, education = %s, employee_position = %s
                WHERE first_name = %s AND surname = %s AND patronymic = %s AND 
                subdivision = %s AND nationality = %s AND education = %s AND employee_position = %s"""
        database.cursor.execute(query, self.get_parameters() + database.copiedEmployee)
        self.output_employees()

interface = Interface()

sys.exit(app.exec_())
