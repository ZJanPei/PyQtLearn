from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui,QtCore
from ui_MainWindow import Ui_MainWindow
from login import Login
from dataPaint import DataPaint

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import pyqtgraph as pg
import tushare as ts  
import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    '''主界面'''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.LoginpushButton.clicked.connect(self.LoginClicked)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontalLayout.addWidget(self.canvas)

        self.paintpushButton.clicked.connect(self.paintBtnClicked)

        self.verticalLayout.addWidget(chart())

        self.show()

    def LoginClicked(self):
        '''处理登录按键，弹出登录对话框'''

        self.login = Login()

    def paintBtnClicked(self):

        print('paint msg received.')

        ax = self.figure.add_axes([0.1,0.1,0.8,0.8])
        ax.set_xlim([-1,6])
        ax.set_ylim([-1,6])
        ax.plot([0,1,2,3,4,5],'o--')

        cavans = FigureCanvas(self.figure)

        #self.canvas = DataPaint.paintLine()
        
        self.canvas.draw()

        self.figure.savefig("examples.jpg")  
        plt.close()
       
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()
 
    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setBrush(pg.mkBrush('r'))
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
 
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
 
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

def chart():
    hist_data = ts.get_hist_data('600519',start='2017-05-01',end='2017-11-24')
    data_list = []
    for dates,row in hist_data.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
        print(date_time)
        #t = date2num(date_time)
        t = 11
        # t = dict(enumerate(datetime))
        open,high,close,low = row[:4]
        datas = (t,open,close,low,high)
        data_list.append(datas)
    #axis_dict = dict(enumerate(axis))
    item = CandlestickItem(data_list)
    plt = pg.PlotWidget()
    plt.addItem(item,)
    plt.showGrid(x=True,y=True)
    return plt

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
