import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    ''' '''

    def __init__(self):
        ''' '''
        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''
        self.setGeometry(100,200,300,400)

        self.setWindowTitle('Icon')

        self.setWindowIcon(QIcon('startup.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
