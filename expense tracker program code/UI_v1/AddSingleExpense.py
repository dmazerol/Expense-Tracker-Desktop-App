# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\AddSingleExpense.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window_addExpenses(object):
    def setupUi(self, window_addExpenses):
        window_addExpenses.setObjectName("window_addExpenses")
        window_addExpenses.resize(597, 421)
        window_addExpenses.setStyleSheet("background-color: rgb(187, 189, 229);\n"
"border-color: rgb(12, 12, 12);")
        self.cbo_userHousehold = QtWidgets.QComboBox(window_addExpenses)
        self.cbo_userHousehold.setGeometry(QtCore.QRect(260, 120, 200, 30))
        self.cbo_userHousehold.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbo_userHousehold.setObjectName("cbo_userHousehold")
        self.radio_personal = QtWidgets.QRadioButton(window_addExpenses)
        self.radio_personal.setGeometry(QtCore.QRect(260, 70, 141, 30))
        self.radio_personal.setObjectName("radio_personal")
        self.btn_groupType = QtWidgets.QButtonGroup(window_addExpenses)
        self.btn_groupType.setObjectName("btn_groupType")
        self.btn_groupType.addButton(self.radio_personal)
        self.radio_combined = QtWidgets.QRadioButton(window_addExpenses)
        self.radio_combined.setGeometry(QtCore.QRect(330, 70, 171, 30))
        self.radio_combined.setObjectName("radio_combined")
        self.btn_groupType.addButton(self.radio_combined)
        self.cmd_upload = QtWidgets.QCommandLinkButton(window_addExpenses)
        self.cmd_upload.setGeometry(QtCore.QRect(15, 370, 221, 41))
        self.cmd_upload.setObjectName("cmd_upload")
        self.lbl_success = QtWidgets.QLabel(window_addExpenses)
        self.lbl_success.setGeometry(QtCore.QRect(290, 373, 1181, 30))
        self.lbl_success.setObjectName("lbl_success")
        self.label = QtWidgets.QLabel(window_addExpenses)
        self.label.setGeometry(QtCore.QRect(20, 70, 221, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(window_addExpenses)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 221, 30))
        self.label_2.setObjectName("label_2")
        self.date_expense = QtWidgets.QDateEdit(window_addExpenses)
        self.date_expense.setGeometry(QtCore.QRect(260, 170, 110, 30))
        self.date_expense.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_expense.setObjectName("date_expense")
        self.label_3 = QtWidgets.QLabel(window_addExpenses)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 221, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(window_addExpenses)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 221, 30))
        self.label_4.setObjectName("label_4")
        self.txt_statement = QtWidgets.QTextEdit(window_addExpenses)
        self.txt_statement.setGeometry(QtCore.QRect(260, 220, 191, 30))
        self.txt_statement.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_statement.setObjectName("txt_statement")
        self.label_5 = QtWidgets.QLabel(window_addExpenses)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 221, 30))
        self.label_5.setObjectName("label_5")
        self.txt_amount = QtWidgets.QLineEdit(window_addExpenses)
        self.txt_amount.setGeometry(QtCore.QRect(260, 270, 113, 30))
        self.txt_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_amount.setObjectName("txt_amount")
        self.radio_expense = QtWidgets.QRadioButton(window_addExpenses)
        self.radio_expense.setGeometry(QtCore.QRect(390, 270, 141, 16))
        self.radio_expense.setObjectName("radio_expense")
        self.btn_groupAmount = QtWidgets.QButtonGroup(window_addExpenses)
        self.btn_groupAmount.setObjectName("btn_groupAmount")
        self.btn_groupAmount.addButton(self.radio_expense)
        self.radio_income = QtWidgets.QRadioButton(window_addExpenses)
        self.radio_income.setGeometry(QtCore.QRect(390, 285, 131, 16))
        self.radio_income.setObjectName("radio_income")
        self.btn_groupAmount.addButton(self.radio_income)
        self.label_6 = QtWidgets.QLabel(window_addExpenses)
        self.label_6.setGeometry(QtCore.QRect(20, 320, 221, 30))
        self.label_6.setObjectName("label_6")
        self.txt_statement_2 = QtWidgets.QTextEdit(window_addExpenses)
        self.txt_statement_2.setGeometry(QtCore.QRect(260, 320, 191, 30))
        self.txt_statement_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_statement_2.setObjectName("txt_statement_2")
        self.label_7 = QtWidgets.QLabel(window_addExpenses)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 581, 41))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(window_addExpenses)
        QtCore.QMetaObject.connectSlotsByName(window_addExpenses)

    def retranslateUi(self, window_addExpenses):
        _translate = QtCore.QCoreApplication.translate
        window_addExpenses.setWindowTitle(_translate("window_addExpenses", "Dialog"))
        self.radio_personal.setText(_translate("window_addExpenses", "Personal"))
        self.radio_combined.setText(_translate("window_addExpenses", "Combined/Household"))
        self.cmd_upload.setText(_translate("window_addExpenses", "Upload Transaction to Database"))
        self.lbl_success.setText(_translate("window_addExpenses", "<html><head/><body><p><span style=\" font-weight:600;\">TextLabel</span></p></body></html>"))
        self.label.setText(_translate("window_addExpenses", "What type of transaction is being added? *"))
        self.label_2.setText(_translate("window_addExpenses", "Name of user / household *"))
        self.label_3.setText(_translate("window_addExpenses", "Date of Transaction *"))
        self.label_4.setToolTip(_translate("window_addExpenses", "<html><head/><body><p>Enter either a sentence or keywords to describe the transaction. The words that are selected in this description are ultimately used to classify the transactions, so select words accordingly.</p><p><br/></p><p>Ex. amazon purchase, loblaws groceries, esso gas, etc.</p></body></html>"))
        self.label_4.setText(_translate("window_addExpenses", "Statement Description (hover for more info) *"))
        self.label_5.setText(_translate("window_addExpenses", "Amount (CDN) *"))
        self.radio_expense.setText(_translate("window_addExpenses", "Expense"))
        self.radio_income.setText(_translate("window_addExpenses", "Income"))
        self.label_6.setToolTip(_translate("window_addExpenses", "<html><head/><body><p>Enter either a sentence or keywords to describe the the type of transaction. This may be used to describe bill payments, rent/mortgage payments, condo fees, etc. </p><p>Default is to leave this field blank for credit card transactions</p></body></html>"))
        self.label_6.setText(_translate("window_addExpenses", "Transaction Type (hover for more info)"))
        self.label_7.setText(_translate("window_addExpenses", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Enter single expenses/revenue transactions by filling out the form below and uploading to database once complete</span></p></body></html>"))

