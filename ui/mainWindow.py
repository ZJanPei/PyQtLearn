from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui,QtCore
from ui_MainWindow import Ui_MainWindow
from login import Login
from dataPaint import DataPaint

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.lines import Line2D
import matplotlib.animation as animation
import numpy as np

import pyqtgraph as pg
import tushare as ts  
import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    '''主界面'''
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.LoginpushButton.clicked.connect(self.LoginClicked)

        self.paintpushButton.clicked.connect(self.paintBtnClicked)

        self.paintBtn_1.clicked.connect(self.paintBtn_1Clicked)

        self.paintBtn_2.clicked.connect(self.paintBtn_2Clicked)

        self.show()


    def LoginClicked(self):
        '''处理登录按键，弹出登录对话框'''

        self.login = Login()

    def paintBtnClicked(self):
        ''' '''

        print('paint button msg rec!')


    def paintBtn_1Clicked(self):

        self.widget.paintTest()

    def paintBtn_2Clicked(self):

        self.widget_2.paintTest()




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
