import sys
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from config import host, username, password, db_name

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())