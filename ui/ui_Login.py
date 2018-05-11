# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(342, 279)
        self.CancelpushButton = QtWidgets.QPushButton(Login)
        self.CancelpushButton.setGeometry(QtCore.QRect(50, 200, 101, 41))
        self.CancelpushButton.setObjectName("CancelpushButton")
        self.OKpushButton = QtWidgets.QPushButton(Login)
        self.OKpushButton.setGeometry(QtCore.QRect(190, 200, 101, 41))
        self.OKpushButton.setObjectName("OKpushButton")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(50, 50, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 51, 31))
        self.label_2.setObjectName("label_2")
        self.RecordNamePWDcheckBox = QtWidgets.QCheckBox(Login)
        self.RecordNamePWDcheckBox.setGeometry(QtCore.QRect(50, 150, 141, 31))
        self.RecordNamePWDcheckBox.setObjectName("RecordNamePWDcheckBox")
        self.UserNamelineEdit = QtWidgets.QLineEdit(Login)
        self.UserNamelineEdit.setGeometry(QtCore.QRect(130, 50, 161, 31))
        self.UserNamelineEdit.setObjectName("UserNamelineEdit")
        self.PWDlineEdit = QtWidgets.QLineEdit(Login)
        self.PWDlineEdit.setGeometry(QtCore.QRect(130, 100, 161, 31))
        self.PWDlineEdit.setObjectName("PWDlineEdit")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录"))
        self.CancelpushButton.setText(_translate("Login", "取消"))
        self.OKpushButton.setText(_translate("Login", "确定"))
        self.label.setText(_translate("Login", "用户名："))
        self.label_2.setText(_translate("Login", "密码："))
        self.RecordNamePWDcheckBox.setText(_translate("Login", "记住用户名和密码"))

