import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.lines as line
import matplotlib.animation as animation


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

         # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # 此处初始化子图一定要在初始化函数之前
        self.fig = plt.figure()
        # 这里坐标范围的设置是为了满足波形信号的波动范围
        self.rt_ax = plt.subplot(111,xlim=(-10,10), ylim=(-20,20))
        #self.rt_ax = plt.subplot(111)
        self.rt_ax.grid(True)


        # 关闭坐标显示
        #plt.axis('off')

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        self.fig.suptitle('波形曲线')

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

        self.rt_line = line.Line2D([],[])
        self.step = 1
        self.t = np.arange(-10, self.step-10, 1)
        self.s =  self.t*2
        self.rt_line.set_xdata(self.t)# 初始化横坐标
        self.rt_line.set_ydata(self.s) # 初始化纵坐标

        self.ani = animation.FuncAnimation(self.mpl.fig, self.plot_update,
                              init_func=self.plot_init, 
                              frames=1,
                              interval=30,
                              blit=True)
        
        self.mpl.draw()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=15, height=15, dpi=100)
        self.layout.addWidget(self.mpl)

    def paintTest(self):

        if self.step>= 20:
            self.step= 1

        else:
            self.step+= 1

        self.t = np.arange(-10, self.step-10, 1)
        self.s =  self.t*2

        print(self.t)
        print(self.s)
        print(self.step)

    def plot_init(self):
        self.mpl.rt_ax.add_line(self.rt_line)
        return self.rt_line,

    def plot_update(self, i):
        self.rt_line.set_xdata(self.t)
        self.rt_line.set_ydata(self.s)
        return self.rt_line,



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())
