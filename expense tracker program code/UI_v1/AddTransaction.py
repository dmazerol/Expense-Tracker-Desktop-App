# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\AddTransaction.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window_addTransaction(object):
    def setupUi(self, window_addTransaction):
        window_addTransaction.setObjectName("window_addTransaction")
        window_addTransaction.resize(759, 458)
        window_addTransaction.setStyleSheet("background-color: rgb(187, 189, 229);\n"
"border-color: rgb(12, 12, 12);")
        self.cbo_userHousehold = QtWidgets.QComboBox(window_addTransaction)
        self.cbo_userHousehold.setGeometry(QtCore.QRect(300, 120, 200, 30))
        self.cbo_userHousehold.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbo_userHousehold.setObjectName("cbo_userHousehold")
        self.radio_personal = QtWidgets.QRadioButton(window_addTransaction)
        self.radio_personal.setGeometry(QtCore.QRect(300, 70, 101, 30))
        self.radio_personal.setObjectName("radio_personal")
        self.btn_groupType = QtWidgets.QButtonGroup(window_addTransaction)
        self.btn_groupType.setObjectName("btn_groupType")
        self.btn_groupType.addButton(self.radio_personal)
        self.radio_combined = QtWidgets.QRadioButton(window_addTransaction)
        self.radio_combined.setGeometry(QtCore.QRect(410, 70, 171, 30))
        self.radio_combined.setObjectName("radio_combined")
        self.btn_groupType.addButton(self.radio_combined)
        self.cmd_upload = QtWidgets.QCommandLinkButton(window_addTransaction)
        self.cmd_upload.setGeometry(QtCore.QRect(15, 370, 271, 41))
        self.cmd_upload.setObjectName("cmd_upload")
        self.label = QtWidgets.QLabel(window_addTransaction)
        self.label.setGeometry(QtCore.QRect(20, 70, 251, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(window_addTransaction)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 221, 30))
        self.label_2.setObjectName("label_2")
        self.date_expense = QtWidgets.QDateEdit(window_addTransaction)
        self.date_expense.setGeometry(QtCore.QRect(300, 170, 110, 30))
        self.date_expense.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_expense.setObjectName("date_expense")
        self.label_3 = QtWidgets.QLabel(window_addTransaction)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 221, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(window_addTransaction)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 271, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(window_addTransaction)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 221, 30))
        self.label_5.setObjectName("label_5")
        self.txt_amount = QtWidgets.QLineEdit(window_addTransaction)
        self.txt_amount.setGeometry(QtCore.QRect(300, 270, 113, 30))
        self.txt_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_amount.setObjectName("txt_amount")
        self.radio_expense = QtWidgets.QRadioButton(window_addTransaction)
        self.radio_expense.setGeometry(QtCore.QRect(430, 268, 141, 16))
        self.radio_expense.setObjectName("radio_expense")
        self.btn_groupAmount = QtWidgets.QButtonGroup(window_addTransaction)
        self.btn_groupAmount.setObjectName("btn_groupAmount")
        self.btn_groupAmount.addButton(self.radio_expense)
        self.radio_income = QtWidgets.QRadioButton(window_addTransaction)
        self.radio_income.setGeometry(QtCore.QRect(430, 287, 131, 16))
        self.radio_income.setObjectName("radio_income")
        self.btn_groupAmount.addButton(self.radio_income)
        self.label_6 = QtWidgets.QLabel(window_addTransaction)
        self.label_6.setGeometry(QtCore.QRect(20, 320, 251, 30))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(window_addTransaction)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 731, 41))
        self.label_7.setObjectName("label_7")
        self.txt_statement = QtWidgets.QLineEdit(window_addTransaction)
        self.txt_statement.setGeometry(QtCore.QRect(300, 220, 351, 30))
        self.txt_statement.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_statement.setObjectName("txt_statement")
        self.txt_type = QtWidgets.QLineEdit(window_addTransaction)
        self.txt_type.setGeometry(QtCore.QRect(300, 320, 351, 30))
        self.txt_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_type.setObjectName("txt_type")

        self.retranslateUi(window_addTransaction)
        QtCore.QMetaObject.connectSlotsByName(window_addTransaction)

    def retranslateUi(self, window_addTransaction):
        _translate = QtCore.QCoreApplication.translate
        window_addTransaction.setWindowTitle(_translate("window_addTransaction", "Dialog"))
        self.radio_personal.setText(_translate("window_addTransaction", "Personal"))
        self.radio_combined.setText(_translate("window_addTransaction", "Combined/Household"))
        self.cmd_upload.setText(_translate("window_addTransaction", "Upload Transaction to Database"))
        self.label.setText(_translate("window_addTransaction", "What type of transaction is being added? *"))
        self.label_2.setText(_translate("window_addTransaction", "Name of user / household *"))
        self.label_3.setText(_translate("window_addTransaction", "Date of Transaction *"))
        self.label_4.setToolTip(_translate("window_addTransaction", "<html><head/><body><p>Enter either a sentence or keywords to describe the transaction. The words that are selected in this description are ultimately used to classify the transactions, so select words accordingly.</p><p><br/></p><p>Ex. amazon purchase, loblaws groceries, esso gas, etc.</p></body></html>"))
        self.label_4.setText(_translate("window_addTransaction", "Statement Description (hover for more info) *"))
        self.label_5.setText(_translate("window_addTransaction", "Amount (CDN) *"))
        self.radio_expense.setText(_translate("window_addTransaction", "Expense"))
        self.radio_income.setText(_translate("window_addTransaction", "Income"))
        self.label_6.setToolTip(_translate("window_addTransaction", "<html><head/><body><p>Enter either a sentence or keywords to describe the the type of transaction. This may be used to describe bill payments, rent/mortgage payments, condo fees, etc. </p><p>Default is to leave this field blank for credit card transactions</p></body></html>"))
        self.label_6.setText(_translate("window_addTransaction", "Transaction Type (hover for more info)"))
        self.label_7.setText(_translate("window_addTransaction", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Enter single expenses/revenue transactions by filling out the form below and uploading to database once complete</span></p></body></html>"))

