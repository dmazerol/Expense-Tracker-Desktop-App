# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\MessageBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        MessageBox.setObjectName("MessageBox")
        MessageBox.setWindowModality(QtCore.Qt.ApplicationModal)
        MessageBox.resize(600, 252)
        self.lbl_message = QtWidgets.QLabel(MessageBox)
        self.lbl_message.setGeometry(QtCore.QRect(10, 30, 580, 150))
        self.lbl_message.setObjectName("lbl_message")
        self.push_OK = QtWidgets.QPushButton(MessageBox)
        self.push_OK.setGeometry(QtCore.QRect(200, 200, 200, 40))
        self.push_OK.setObjectName("push_OK")
        self.cbo_cats = QtWidgets.QComboBox(MessageBox)
        self.cbo_cats.setGeometry(QtCore.QRect(30, 160, 250, 30))
        self.cbo_cats.setStyleSheet("background-color: rgb(167, 176, 168);")
        self.cbo_cats.setObjectName("cbo_cats")
        self.txt_newCat = QtWidgets.QLineEdit(MessageBox)
        self.txt_newCat.setGeometry(QtCore.QRect(300, 160, 250, 30))
        self.txt_newCat.setObjectName("txt_newCat")
        self.push_cancel = QtWidgets.QPushButton(MessageBox)
        self.push_cancel.setGeometry(QtCore.QRect(20, 200, 141, 40))
        self.push_cancel.setObjectName("push_cancel")

        self.retranslateUi(MessageBox)
        QtCore.QMetaObject.connectSlotsByName(MessageBox)

    def retranslateUi(self, MessageBox):
        _translate = QtCore.QCoreApplication.translate
        MessageBox.setWindowTitle(_translate("MessageBox", "Dialog"))
        self.lbl_message.setText(_translate("MessageBox", "<html><head/><body><p><br/></p></body></html>"))
        self.push_OK.setText(_translate("MessageBox", "OK"))
        self.push_cancel.setText(_translate("MessageBox", "Cancel"))

