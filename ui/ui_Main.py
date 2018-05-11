# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(400, 300)
        self.LoginpushButton = QtWidgets.QPushButton(Main)
        self.LoginpushButton.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.LoginpushButton.setObjectName("LoginpushButton")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.LoginpushButton.setText(_translate("Main", "登录"))

