import sys
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from config import host, user, password, database

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

class Database:
    def __init__(self, connection):
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
                VALUES (%s, %s, %s, %s, %s, %s %s)"""
        database.cursor.execute(query, parameters)


interface = Interface()

sys.exit(app.exec_())