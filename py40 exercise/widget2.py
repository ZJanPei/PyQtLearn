import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''

        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        ''' '''

        pixmap = QPixmap('lena.png')

        hbox = QHBoxLayout(self)

        label = QLabel(self)
        label.setPixmap(pixmap)

        self.textlabel = QLabel(self)
        lineedit = QLineEdit(self)

        lineedit.textChanged[str].connect(self.onChanged)

        hbox.addWidget(label)
        hbox.addWidget(self.textlabel)
        hbox.addWidget(lineedit)

        self.setLayout(hbox)

    def onChanged(self, text):
        ''' '''
        
        self.textlabel.setText(text)
        self.textlabel.adjustSize()
        

    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:
            self.close()

class Example1(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        ''' ''' 

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright= QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        spliter1 = QSplitter(Qt.Horizontal)
        spliter1.addWidget(topleft)
        spliter1.addWidget(topright)

        spliter2 = QSplitter(Qt.Vertical)
        spliter2.addWidget(spliter1)
        spliter2.addWidget(bottom)

        hbox.addWidget(spliter2)
        self.setLayout(hbox)

        self.label = QLabel('Ubuntu', self)

        combo = QComboBox(self)
        combo.addItem('1')
        combo.addItem('2')
        combo.addItem('3')
        combo.addItem('4')
        combo.addItem('5')
        combo.addItem('6')

        hbox.addWidget(self.label)
        hbox.addWidget(combo)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('控件')

    def onActivated(self, text):
        ''' '''
        
        self.label.setText(text)
        self.label.adjustSize()

    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = Example()
    ex1 = Example1()
    sys.exit(app.exec_())
