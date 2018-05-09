import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    ''' '''

    def __init__(self):
        ''' '''

        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''

        btn = QPushButton('Quit', self)

        btn.resize(btn.sizeHint())

        btn.move(100,100)

        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(500, 500, 500, 500)

        self.setWindowTitle('Quit Button')

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

