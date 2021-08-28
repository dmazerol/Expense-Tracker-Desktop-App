# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_v1\results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1247, 653)
        self.tab_byMonthYear = QtWidgets.QTabWidget(Dialog)
        self.tab_byMonthYear.setGeometry(QtCore.QRect(10, 20, 701, 561))
        self.tab_byMonthYear.setObjectName("tab_byMonthYear")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_byMonth = QtWidgets.QTableWidget(self.tab)
        self.table_byMonth.setGeometry(QtCore.QRect(10, 10, 651, 511))
        self.table_byMonth.setObjectName("table_byMonth")
        self.table_byMonth.setColumnCount(5)
        self.table_byMonth.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_byMonth.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byMonth.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byMonth.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byMonth.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byMonth.setHorizontalHeaderItem(4, item)
        self.tab_byMonthYear.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table_byYear = QtWidgets.QTableWidget(self.tab_2)
        self.table_byYear.setGeometry(QtCore.QRect(10, 10, 661, 511))
        self.table_byYear.setObjectName("table_byYear")
        self.table_byYear.setColumnCount(5)
        self.table_byYear.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_byYear.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byYear.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byYear.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byYear.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_byYear.setHorizontalHeaderItem(4, item)
        self.tab_byMonthYear.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tab_byMonthYear.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.table_byMonth.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Category"))
        item = self.table_byMonth.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Average (CDN)"))
        item = self.table_byMonth.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Median (CDN)"))
        item = self.table_byMonth.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "STD (CDN)"))
        item = self.table_byMonth.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Count"))
        self.tab_byMonthYear.setTabText(self.tab_byMonthYear.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        item = self.table_byYear.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Category"))
        item = self.table_byYear.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Average (CDN)"))
        item = self.table_byYear.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Median (CDN)"))
        item = self.table_byYear.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "STD (CDN)"))
        item = self.table_byYear.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Count"))
        self.tab_byMonthYear.setTabText(self.tab_byMonthYear.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))

