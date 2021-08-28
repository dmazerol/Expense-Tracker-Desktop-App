# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 422)
        MainWindow.setStyleSheet("background-color: rgb(162, 240, 200);\n"
"border-color: rgb(12, 12, 12);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_endDate = QtWidgets.QLabel(self.centralwidget)
        self.lbl_endDate.setGeometry(QtCore.QRect(10, 240, 100, 25))
        self.lbl_endDate.setObjectName("lbl_endDate")
        self.lbl_selectInd = QtWidgets.QLabel(self.centralwidget)
        self.lbl_selectInd.setGeometry(QtCore.QRect(10, 40, 100, 25))
        self.lbl_selectInd.setObjectName("lbl_selectInd")
        self.command_analyzeExpenses = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.command_analyzeExpenses.setGeometry(QtCore.QRect(10, 290, 350, 40))
        self.command_analyzeExpenses.setStyleSheet("border-color: rgb(12, 12, 12);")
        self.command_analyzeExpenses.setObjectName("command_analyzeExpenses")
        self.date_endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.date_endDate.setGeometry(QtCore.QRect(120, 240, 120, 25))
        self.date_endDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_endDate.setCalendarPopup(True)
        self.date_endDate.setCurrentSectionIndex(0)
        self.date_endDate.setDate(QtCore.QDate(2000, 1, 1))
        self.date_endDate.setObjectName("date_endDate")
        self.date_startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.date_startDate.setGeometry(QtCore.QRect(120, 190, 120, 25))
        self.date_startDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_startDate.setCalendarPopup(True)
        self.date_startDate.setDate(QtCore.QDate(2000, 1, 1))
        self.date_startDate.setObjectName("date_startDate")
        self.radio_incHousehold = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_incHousehold.setGeometry(QtCore.QRect(10, 80, 250, 25))
        self.radio_incHousehold.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.radio_incHousehold.setObjectName("radio_incHousehold")
        self.lbl_startDate = QtWidgets.QLabel(self.centralwidget)
        self.lbl_startDate.setGeometry(QtCore.QRect(10, 190, 100, 25))
        self.lbl_startDate.setObjectName("lbl_startDate")
        self.lbl_splitRatio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_splitRatio.setGeometry(QtCore.QRect(10, 130, 150, 25))
        self.lbl_splitRatio.setObjectName("lbl_splitRatio")
        self.numb_ratio = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.numb_ratio.setGeometry(QtCore.QRect(170, 130, 75, 25))
        self.numb_ratio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numb_ratio.setDecimals(1)
        self.numb_ratio.setMaximum(1.0)
        self.numb_ratio.setProperty("value", 0.0)
        self.numb_ratio.setObjectName("numb_ratio")
        self.cbo_userDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.cbo_userDropdown.setGeometry(QtCore.QRect(120, 40, 250, 25))
        self.cbo_userDropdown.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbo_userDropdown.setObjectName("cbo_userDropdown")
        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setGeometry(QtCore.QRect(10, 0, 350, 25))
        self.lbl_info.setObjectName("lbl_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color: rgb(167, 176, 168);\n"
"border-color: rgb(12, 12, 12);")
        self.menubar.setObjectName("menubar")
        self.menuUtilities = QtWidgets.QMenu(self.menubar)
        self.menuUtilities.setObjectName("menuUtilities")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_addUser = QtWidgets.QAction(MainWindow)
        self.action_addUser.setObjectName("action_addUser")
        self.action_addTransaction = QtWidgets.QAction(MainWindow)
        self.action_addTransaction.setObjectName("action_addTransaction")
        self.action_removeCat = QtWidgets.QAction(MainWindow)
        self.action_removeCat.setObjectName("action_removeCat")
        self.action_removeCatEntry = QtWidgets.QAction(MainWindow)
        self.action_removeCatEntry.setObjectName("action_removeCatEntry")
        self.action_addTransactionS = QtWidgets.QAction(MainWindow)
        self.action_addTransactionS.setObjectName("action_addTransactionS")
        self.actionExit_Application = QtWidgets.QAction(MainWindow)
        self.actionExit_Application.setObjectName("actionExit_Application")
        self.action_exportToExcel = QtWidgets.QAction(MainWindow)
        self.action_exportToExcel.setObjectName("action_exportToExcel")
        self.actionExport_Results_to_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_Results_to_CSV.setObjectName("actionExport_Results_to_CSV")
        self.action_goToMain = QtWidgets.QAction(MainWindow)
        self.action_goToMain.setObjectName("action_goToMain")
        self.action_resetData = QtWidgets.QAction(MainWindow)
        self.action_resetData.setObjectName("action_resetData")
        self.action_resultsWindow = QtWidgets.QAction(MainWindow)
        self.action_resultsWindow.setObjectName("action_resultsWindow")
        self.menuUtilities.addAction(self.action_addUser)
        self.menuUtilities.addAction(self.action_addTransaction)
        self.menuUtilities.addAction(self.action_addTransactionS)
        self.menuUtilities.addAction(self.action_removeCat)
        self.menuUtilities.addAction(self.action_removeCatEntry)
        self.menuExit.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuUtilities.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_endDate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">End Date</span></p></body></html>"))
        self.lbl_selectInd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Select User</span></p></body></html>"))
        self.command_analyzeExpenses.setText(_translate("MainWindow", "Analyze Expenses"))
        self.radio_incHousehold.setText(_translate("MainWindow", "Include Combined Household Expenses?"))
        self.lbl_startDate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Start Date</span></p></body></html>"))
        self.lbl_splitRatio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Household Split Ratio</span></p></body></html>"))
        self.lbl_info.setText(_translate("MainWindow", "Enter parameters below for expenses to be tracked"))
        self.menuUtilities.setTitle(_translate("MainWindow", "Utilities"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_addUser.setText(_translate("MainWindow", "Add User"))
        self.action_addTransaction.setText(_translate("MainWindow", "Add Single Transaction"))
        self.action_removeCat.setText(_translate("MainWindow", "Remove a Category"))
        self.action_removeCatEntry.setText(_translate("MainWindow", "Remove a Categorical Entry"))
        self.action_addTransactionS.setText(_translate("MainWindow", "Add Transaction Banking Statements"))
        self.actionExit_Application.setText(_translate("MainWindow", "Exit Application"))
        self.action_exportToExcel.setText(_translate("MainWindow", "Export Results to Excel"))
        self.actionExport_Results_to_CSV.setText(_translate("MainWindow", "Export Results to CSV"))
        self.action_goToMain.setText(_translate("MainWindow", "Go to Main Window"))
        self.action_resetData.setText(_translate("MainWindow", "Reset Data"))
        self.action_resultsWindow.setText(_translate("MainWindow", "Results Window"))
