# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\errorbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorBox(object):
    def setupUi(self, ErrorBox):
        ErrorBox.setObjectName("ErrorBox")
        ErrorBox.setWindowModality(QtCore.Qt.ApplicationModal)
        ErrorBox.resize(420, 259)
        self.lbl_errorMessage = QtWidgets.QLabel(ErrorBox)
        self.lbl_errorMessage.setGeometry(QtCore.QRect(10, 30, 401, 121))
        self.lbl_errorMessage.setObjectName("lbl_errorMessage")
        self.push_OK = QtWidgets.QPushButton(ErrorBox)
        self.push_OK.setGeometry(QtCore.QRect(142, 207, 141, 41))
        self.push_OK.setObjectName("push_OK")

        self.retranslateUi(ErrorBox)
        QtCore.QMetaObject.connectSlotsByName(ErrorBox)

    def retranslateUi(self, ErrorBox):
        _translate = QtCore.QCoreApplication.translate
        ErrorBox.setWindowTitle(_translate("ErrorBox", "Dialog"))
        self.lbl_errorMessage.setText(_translate("ErrorBox", "<html><head/><body><p><br/></p></body></html>"))
        self.push_OK.setText(_translate("ErrorBox", "OK"))

