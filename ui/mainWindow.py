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
        self.fig, self.ax1 = plt.subplots()
        self.scope = Scope(self.ax1)

        self.setupUi(self)

        self.LoginpushButton.clicked.connect(self.LoginClicked)

        #self.fig, self.ax1 = plt.subplots()
        #self.scope = Scope(self.ax1)

        self.canvas = FigureCanvas(self.fig)
        self.horizontalLayout.addWidget(self.canvas)

        self.ani = animation.FuncAnimation(self.fig, self.scope.update, emitter, interval=10, blit=True)

        self.show()

        self.paintpushButton.clicked.connect(self.paintBtnClicked)

    def LoginClicked(self):
        '''处理登录按键，弹出登录对话框'''

        self.login = Login()

    def paintBtnClicked(self):

        self.canvas.draw()

        #self.ani = animation.FuncAnimation(self.fig, self.scope.update, emitter, interval=10, blit=True)

        #self.fig.savefig("examples.jpg")  
        #plt.close()

class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        print('Here')
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,
def emitter(p=0.03):
    'return a random value with probability p, else 0'
    while True:
        v = np.random.rand(1)
        if v > p:
            yield 0.
        else:
            yield np.random.rand(1)

# Fixing random state for reproducibility
np.random.seed(19680801)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
