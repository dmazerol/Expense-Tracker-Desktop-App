# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\add_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(492, 300)
        AddUser.setStyleSheet("background-color: rgb(187, 189, 229);\n"
"border-color: rgb(12, 12, 12);")
        self.lbl_promptUser = QtWidgets.QLabel(AddUser)
        self.lbl_promptUser.setGeometry(QtCore.QRect(10, 30, 271, 25))
        self.lbl_promptUser.setObjectName("lbl_promptUser")
        self.txt_user = QtWidgets.QLineEdit(AddUser)
        self.txt_user.setGeometry(QtCore.QRect(280, 27, 201, 25))
        self.txt_user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_user.setObjectName("txt_user")
        self.lbl_combinedExpenses = QtWidgets.QLabel(AddUser)
        self.lbl_combinedExpenses.setGeometry(QtCore.QRect(10, 80, 391, 25))
        self.lbl_combinedExpenses.setObjectName("lbl_combinedExpenses")
        self.radio_yesCombined = QtWidgets.QRadioButton(AddUser)
        self.radio_yesCombined.setGeometry(QtCore.QRect(10, 110, 61, 25))
        self.radio_yesCombined.setObjectName("radio_yesCombined")
        self.radio_noCombined = QtWidgets.QRadioButton(AddUser)
        self.radio_noCombined.setGeometry(QtCore.QRect(70, 110, 71, 25))
        self.radio_noCombined.setChecked(True)
        self.radio_noCombined.setObjectName("radio_noCombined")
        self.push_register = QtWidgets.QPushButton(AddUser)
        self.push_register.setGeometry(QtCore.QRect(250, 260, 100, 25))
        self.push_register.setObjectName("push_register")
        self.push_cancel = QtWidgets.QPushButton(AddUser)
        self.push_cancel.setGeometry(QtCore.QRect(372, 260, 100, 25))
        self.push_cancel.setObjectName("push_cancel")
        self.lbl_householdOption = QtWidgets.QLabel(AddUser)
        self.lbl_householdOption.setGeometry(QtCore.QRect(10, 160, 181, 81))
        self.lbl_householdOption.setObjectName("lbl_householdOption")
        self.cbo_household = QtWidgets.QComboBox(AddUser)
        self.cbo_household.setGeometry(QtCore.QRect(200, 160, 200, 25))
        self.cbo_household.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(12, 12, 12);")
        self.cbo_household.setObjectName("cbo_household")
        self.txt_household = QtWidgets.QLineEdit(AddUser)
        self.txt_household.setGeometry(QtCore.QRect(200, 217, 200, 25))
        self.txt_household.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_household.setObjectName("txt_household")

        self.retranslateUi(AddUser)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "Dialog"))
        self.lbl_promptUser.setText(_translate("AddUser", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Name of new user </span>(lowercase only)<span style=\" font-weight:600;\">:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.lbl_combinedExpenses.setText(_translate("AddUser", "<html><head/><body><p>Does this new user have combined expenses </br> as part of household?</p></body></html>"))
        self.radio_yesCombined.setText(_translate("AddUser", "yes"))
        self.radio_noCombined.setText(_translate("AddUser", "no"))
        self.push_register.setText(_translate("AddUser", "Register User"))
        self.push_cancel.setText(_translate("AddUser", "Cancel"))
        self.lbl_householdOption.setText(_translate("AddUser", "<html><head/><body><p>Select household name </p><p>or </p><p>create new household name</p></body></html>"))

