# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginpushButton.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.LoginpushButton.setObjectName("LoginpushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 10, 1171, 661))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.Commtab = QtWidgets.QWidget()
        self.Commtab.setObjectName("Commtab")
        self.tabWidget.addTab(self.Commtab, "")
        self.UISettab = QtWidgets.QWidget()
        self.UISettab.setObjectName("UISettab")
        self.tabWidget.addTab(self.UISettab, "")
        self.Analysetab = QtWidgets.QWidget()
        self.Analysetab.setObjectName("Analysetab")
        self.paintpushButton = QtWidgets.QPushButton(self.Analysetab)
        self.paintpushButton.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.paintpushButton.setObjectName("paintpushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Analysetab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 971, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.addTab(self.Analysetab, "")
        self.pygraphtab = QtWidgets.QWidget()
        self.pygraphtab.setObjectName("pygraphtab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.pygraphtab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1071, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.pygraphtab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = MatplotlibWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(220, 20, 841, 241))
        self.widget.setObjectName("widget")
        self.widget_2 = MatplotlibWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(220, 280, 841, 301))
        self.widget_2.setObjectName("widget_2")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "清瑞医疗血糖分析系统"))
        self.LoginpushButton.setText(_translate("MainWindow", "登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Commtab), _translate("MainWindow", "通信设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UISettab), _translate("MainWindow", "电压电流设置"))
        self.paintpushButton.setText(_translate("MainWindow", "绘制"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Analysetab), _translate("MainWindow", "数据分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pygraphtab), _translate("MainWindow", "绘图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

from MatplotlibWidget import MatplotlibWidget
