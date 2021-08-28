# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\AddExpenses.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window_addTransactionS(object):
    def setupUi(self, window_addTransactionS):
        window_addTransactionS.setObjectName("window_addTransactionS")
        window_addTransactionS.resize(1278, 645)
        window_addTransactionS.setStyleSheet("background-color: rgb(187, 189, 229);\n"
"border-color: rgb(12, 12, 12);")
        self.push_uploadCSV = QtWidgets.QPushButton(window_addTransactionS)
        self.push_uploadCSV.setGeometry(QtCore.QRect(20, 20, 300, 30))
        self.push_uploadCSV.setStyleSheet("background-color: rgb(167, 176, 168);")
        self.push_uploadCSV.setObjectName("push_uploadCSV")
        self.cbo_userHousehold = QtWidgets.QComboBox(window_addTransactionS)
        self.cbo_userHousehold.setGeometry(QtCore.QRect(330, 70, 200, 25))
        self.cbo_userHousehold.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbo_userHousehold.setObjectName("cbo_userHousehold")
        self.radio_personal = QtWidgets.QRadioButton(window_addTransactionS)
        self.radio_personal.setGeometry(QtCore.QRect(20, 70, 141, 25))
        self.radio_personal.setObjectName("radio_personal")
        self.radio_combined = QtWidgets.QRadioButton(window_addTransactionS)
        self.radio_combined.setGeometry(QtCore.QRect(160, 70, 171, 25))
        self.radio_combined.setObjectName("radio_combined")
        self.cmd_upload = QtWidgets.QCommandLinkButton(window_addTransactionS)
        self.cmd_upload.setGeometry(QtCore.QRect(604, 63, 321, 41))
        self.cmd_upload.setObjectName("cmd_upload")
        self.table_file = QtWidgets.QTableWidget(window_addTransactionS)
        self.table_file.setGeometry(QtCore.QRect(10, 160, 1251, 411))
        self.table_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_file.setObjectName("table_file")
        self.table_file.setColumnCount(0)
        self.table_file.setRowCount(0)
        self.lbl_uploadCSV = QtWidgets.QLabel(window_addTransactionS)
        self.lbl_uploadCSV.setGeometry(QtCore.QRect(340, 20, 761, 30))
        self.lbl_uploadCSV.setObjectName("lbl_uploadCSV")
        self.lbl_success = QtWidgets.QLabel(window_addTransactionS)
        self.lbl_success.setGeometry(QtCore.QRect(34, 110, 1181, 30))
        self.lbl_success.setObjectName("lbl_success")

        self.retranslateUi(window_addTransactionS)
        QtCore.QMetaObject.connectSlotsByName(window_addTransactionS)

    def retranslateUi(self, window_addTransactionS):
        _translate = QtCore.QCoreApplication.translate
        window_addTransactionS.setWindowTitle(_translate("window_addTransactionS", "Dialog"))
        self.push_uploadCSV.setText(_translate("window_addTransactionS", "Select a csv file to upload it to the application"))
        self.radio_personal.setText(_translate("window_addTransactionS", "Personal Expenses"))
        self.radio_combined.setText(_translate("window_addTransactionS", "Combined Expenses"))
        self.cmd_upload.setText(_translate("window_addTransactionS", "Upload Expenses to Database"))
        self.lbl_uploadCSV.setText(_translate("window_addTransactionS", "the .csv file for import must: 1) Be in column order: Date, Description, Amount, Type (optional). 2) Not have any headers"))
        self.lbl_success.setText(_translate("window_addTransactionS", "<html><head/><body><p><span style=\" font-weight:600;\">TextLabel</span></p></body></html>"))

