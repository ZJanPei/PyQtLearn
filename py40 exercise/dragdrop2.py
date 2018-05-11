import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):
    def __init__(self,title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, event):

        if event.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, event):

        QPushButton.mousePressEvent(self, event)

        if event.button() == Qt.LeftButton:
            print('press')



class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        ''' '''
        self.setAcceptDrops(True)
 
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('控件拖拽2')
        self.setGeometry(300, 300, 300, 200)

    def dragEnterEvent(self, e):
        e.accept()
 
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
 
        e.setDropAction(Qt.MoveAction)
        e.accept()

    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
