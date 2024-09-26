from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(7, 79, 87);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Nirmala UI\";")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchCB = QtWidgets.QComboBox(self.centralwidget)
        self.searchCB.setMinimumSize(QtCore.QSize(140, 20))
        self.searchCB.setStyleSheet("background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;")
        self.searchCB.setObjectName("searchCB")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.searchCB.addItem("")
        self.horizontalLayout.addWidget(self.searchCB)
        self.searchLE = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.searchLE.setObjectName("searchLE")
        self.horizontalLayout.addWidget(self.searchLE)
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.searchBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sortParamCB = QtWidgets.QComboBox(self.centralwidget)
        self.sortParamCB.setMinimumSize(QtCore.QSize(140, 20))
        self.sortParamCB.setStyleSheet("background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;")
        self.sortParamCB.setObjectName("sortParamCB")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.sortParamCB.addItem("")
        self.horizontalLayout.addWidget(self.sortParamCB)
        self.sortOrderCB = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortOrderCB.sizePolicy().hasHeightForWidth())
        self.sortOrderCB.setSizePolicy(sizePolicy)
        self.sortOrderCB.setMinimumSize(QtCore.QSize(100, 20))
        self.sortOrderCB.setStyleSheet("background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;")
        self.sortOrderCB.setObjectName("sortOrderCB")
        self.sortOrderCB.addItem("")
        self.sortOrderCB.addItem("")
        self.horizontalLayout.addWidget(self.sortOrderCB)
        self.sortBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortBtn.sizePolicy().hasHeightForWidth())
        self.sortBtn.setSizePolicy(sizePolicy)
        self.sortBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.sortBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.sortBtn.setObjectName("sortBtn")
        self.horizontalLayout.addWidget(self.sortBtn)
        self.sortResetBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortResetBtn.sizePolicy().hasHeightForWidth())
        self.sortResetBtn.setSizePolicy(sizePolicy)
        self.sortResetBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.sortResetBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.sortResetBtn.setObjectName("sortResetBtn")
        self.horizontalLayout.addWidget(self.sortResetBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordsLabel.setObjectName("recordsLabel")
        self.verticalLayout.addWidget(self.recordsLabel)
        self.personnelTable = QtWidgets.QTableWidget(self.centralwidget)
        self.personnelTable.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(228, 197, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.personnelTable.setObjectName("personnelTable")
        self.personnelTable.setColumnCount(7)
        self.personnelTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.personnelTable)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.firstNameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.firstNameLE.setObjectName("firstNameLE")
        self.gridLayout.addWidget(self.firstNameLE, 0, 2, 1, 1)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy)
        self.addBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.addBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 0, 3, 1, 1)
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.gridLayout.addWidget(self.firstNameLabel, 0, 0, 1, 1)
        self.surnameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.surnameLE.setObjectName("surnameLE")
        self.gridLayout.addWidget(self.surnameLE, 1, 2, 1, 1)
        self.educationLabel = QtWidgets.QLabel(self.centralwidget)
        self.educationLabel.setObjectName("educationLabel")
        self.gridLayout.addWidget(self.educationLabel, 5, 0, 1, 1)
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.gridLayout.addWidget(self.surnameLabel, 1, 0, 1, 1)
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy)
        self.deleteBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.deleteBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout.addWidget(self.deleteBtn, 1, 3, 1, 1)
        self.nationalityLabel = QtWidgets.QLabel(self.centralwidget)
        self.nationalityLabel.setObjectName("nationalityLabel")
        self.gridLayout.addWidget(self.nationalityLabel, 4, 0, 1, 1)
        self.educationLE = QtWidgets.QLineEdit(self.centralwidget)
        self.educationLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.educationLE.setObjectName("educationLE")
        self.gridLayout.addWidget(self.educationLE, 5, 2, 1, 1)
        self.subdivisionLE = QtWidgets.QLineEdit(self.centralwidget)
        self.subdivisionLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.subdivisionLE.setObjectName("subdivisionLE")
        self.gridLayout.addWidget(self.subdivisionLE, 3, 2, 1, 1)
        self.nationalityLE = QtWidgets.QLineEdit(self.centralwidget)
        self.nationalityLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.nationalityLE.setObjectName("nationalityLE")
        self.gridLayout.addWidget(self.nationalityLE, 4, 2, 1, 1)
        self.positionLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLabel.setObjectName("positionLabel")
        self.gridLayout.addWidget(self.positionLabel, 6, 0, 1, 1)
        self.patronymicLabel = QtWidgets.QLabel(self.centralwidget)
        self.patronymicLabel.setObjectName("patronymicLabel")
        self.gridLayout.addWidget(self.patronymicLabel, 2, 0, 1, 1)
        self.positionLE = QtWidgets.QLineEdit(self.centralwidget)
        self.positionLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.positionLE.setObjectName("positionLE")
        self.gridLayout.addWidget(self.positionLE, 6, 2, 1, 1)
        self.patronymicLE = QtWidgets.QLineEdit(self.centralwidget)
        self.patronymicLE.setStyleSheet("border: 2px solid rgb(228, 197, 175);\n"
"border-radius: 10px;")
        self.patronymicLE.setObjectName("patronymicLE")
        self.gridLayout.addWidget(self.patronymicLE, 2, 2, 1, 1)
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy)
        self.editBtn.setMinimumSize(QtCore.QSize(70, 25))
        self.editBtn.setStyleSheet("QPushButton {\n"
"background-color: rgb(116, 165, 127);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(145, 206, 158)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgb(83, 118, 90)\n"
"}")
        self.editBtn.setObjectName("editBtn")
        self.gridLayout.addWidget(self.editBtn, 2, 3, 1, 1)
        self.subdivisionLabel = QtWidgets.QLabel(self.centralwidget)
        self.subdivisionLabel.setObjectName("subdivisionLabel")
        self.gridLayout.addWidget(self.subdivisionLabel, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menuFile.addAction(self.actionSave)
        self.menuAbout.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.personnelTable.setColumnWidth(0, 150)
        self.personnelTable.setColumnWidth(1, 150)
        self.personnelTable.setColumnWidth(2, 150)
        self.personnelTable.setColumnWidth(3, 200)
        self.personnelTable.setColumnWidth(4, 150)
        self.personnelTable.setColumnWidth(5, 100)
        self.personnelTable.setColumnWidth(6, 200)

        self.searchLE.setPlaceholderText("Enter...")
        self.firstNameLE.setPlaceholderText("Enter...")
        self.surnameLE.setPlaceholderText("Enter...")
        self.patronymicLE.setPlaceholderText("Enter...")
        self.subdivisionLE.setPlaceholderText("Enter...")
        self.nationalityLE.setPlaceholderText("Enter...")
        self.educationLE.setPlaceholderText("Enter...")
        self.positionLE.setPlaceholderText("Enter...")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personnel"))
        self.searchCB.setItemText(0, _translate("MainWindow", "First name"))
        self.searchCB.setItemText(1, _translate("MainWindow", "Surname"))
        self.searchCB.setItemText(2, _translate("MainWindow", "Patronymic"))
        self.searchCB.setItemText(3, _translate("MainWindow", "Subdivision"))
        self.searchCB.setItemText(4, _translate("MainWindow", "Nationality"))
        self.searchCB.setItemText(5, _translate("MainWindow", "Education"))
        self.searchCB.setItemText(6, _translate("MainWindow", "Employee position"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.sortParamCB.setItemText(0, _translate("MainWindow", "First name"))
        self.sortParamCB.setItemText(1, _translate("MainWindow", "Surname"))
        self.sortParamCB.setItemText(2, _translate("MainWindow", "Patronymic"))
        self.sortParamCB.setItemText(3, _translate("MainWindow", "Subdivision"))
        self.sortParamCB.setItemText(4, _translate("MainWindow", "Nationality"))
        self.sortParamCB.setItemText(5, _translate("MainWindow", "Education"))
        self.sortParamCB.setItemText(6, _translate("MainWindow", "Employee position"))
        self.sortOrderCB.setItemText(0, _translate("MainWindow", "Ascending"))
        self.sortOrderCB.setItemText(1, _translate("MainWindow", "Descending"))
        self.sortBtn.setText(_translate("MainWindow", "Sort"))
        self.sortResetBtn.setText(_translate("MainWindow", "Reset"))
        self.recordsLabel.setText(_translate("MainWindow", "Total records"))
        item = self.personnelTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First name"))
        item = self.personnelTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.personnelTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Patronymic"))
        item = self.personnelTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Subdivision"))
        item = self.personnelTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nationality"))
        item = self.personnelTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Education"))
        item = self.personnelTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Position"))
        self.addBtn.setText(_translate("MainWindow", "ADD"))
        self.firstNameLabel.setText(_translate("MainWindow", "First name"))
        self.educationLabel.setText(_translate("MainWindow", "Education"))
        self.surnameLabel.setText(_translate("MainWindow", "Surname"))
        self.deleteBtn.setText(_translate("MainWindow", "DELETE"))
        self.nationalityLabel.setText(_translate("MainWindow", "Nationality"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.patronymicLabel.setText(_translate("MainWindow", "Patronymic"))
        self.editBtn.setText(_translate("MainWindow", "EDIT"))
        self.subdivisionLabel.setText(_translate("MainWindow", "Subdivision"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))