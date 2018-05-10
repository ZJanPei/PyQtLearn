import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSignal, QObject 

class Communicate(QObject):

    closeApp = pyqtSignal()


class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''
        lcd = QLCDNumber(self)

        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()

        btn1 = QPushButton('Button 1')

        btn2 = QPushButton('Button 2')

        btnclose = QPushButton('Button Close')

        btn1.clicked.connect(self.buttonClicked)

        btn2.clicked.connect(self.buttonClicked)

        btnclose.clicked.connect(self.buttoncloseClicked)

        self.textedit = QTextEdit()


        self.closesignal = Communicate()

        self.closesignal.closeApp.connect(self.close)


        vbox.addWidget(lcd)

        vbox.addWidget(sld)

        vbox.addWidget(btn1)

        vbox.addWidget(btn2)

        vbox.addWidget(self.textedit)

        vbox.addWidget(btnclose)


        self.setLayout(vbox)

        sld.valueChanged.connect(lcd.display)


        self.setGeometry(300, 300,250,150)

        self.setWindowTitle('Signals & Slots')

        self.show()


    def buttonClicked(self):
        ''' '''
        sender = self.sender()

        self.textedit.insertPlainText(sender.text() + 'was pressed.\n')

        self.textedit.moveCursor(QTextCursor.End) 


    def buttoncloseClicked(self):
        ''' '''

        self.closesignal.closeApp.emit()


    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:

            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
