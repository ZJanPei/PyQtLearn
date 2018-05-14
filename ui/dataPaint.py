import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class DataPaint(object):
    ''' '''
    def __init__(self):
        pass

    def paintLine(self):
        '''绘制测试图像'''
        plt.cla()
        fig = plt.figure()
        ax =fig.add_axes([0.1,0.1,0.8,0.8])
        ax.set_xlim([-1,6])
        ax.set_ylim([-1,6])
        ax.plot([0,1,2,3,4,5],'o--')

        cavans = FigureCanvas(fig)

        return cavans

