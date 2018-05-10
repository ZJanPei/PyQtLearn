import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFrame, QColorDialog, QVBoxLayout, QSizePolicy, QLabel, QFontDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''
        self.btn = QPushButton('Dialog', self)

        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        
        self.colorbtn = QPushButton('Color', self)

        self.colorbtn.move(20, 60)

        self.colorbtn.clicked.connect(self.showColorDialog)


        col = QColor(0, 0, 0)


        fontBtn = QPushButton('Dialog', self)

        fontBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        fontBtn.move(20, 100)

        fontBtn.clicked.connect(self.showFontDialog)


        self.label = QLabel('Knowledge only matters', self)

        self.label.move(130, 105)


        self.frame = QFrame(self)

        self.frame.setStyleSheet('QWidget {background-color:%s}'% col.name())

        self.frame.setGeometry(130, 60,130,20)

        
        self.lineEdit = QLineEdit(self)

        self.lineEdit.move(130,22)


        self.setGeometry(300, 300,300,150)

        self.setWindowTitle('Dialog')

        self.show()

    def showDialog(self):
        ''' '''
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter you name:')

        if ok:
            self.lineEdit.setText(str(text))

    def showColorDialog(self):
        ''' '''

        color = QColorDialog.getColor()

        if color.isValid():

            self.frame.setStyleSheet('QWidget {background-color:%s}'% color.name())
        
    def showFontDialog(self):
        ''' '''
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:

            self.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
