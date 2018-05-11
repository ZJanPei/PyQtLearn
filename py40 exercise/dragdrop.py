import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self,title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        ''' '''
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        ''' '''
        self.setText(event.mimeData().text())


class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        ''' '''
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30,65)
        
        button = Button('Button', self)
        button.move(200, 65)

        self.setWindowTitle('控件拖拽')
        self.setGeometry(300, 300, 300, 200)

    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
