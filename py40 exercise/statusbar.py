import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''

        textEdit = QTextEdit()

        self.setCentralWidget(textEdit)


        exitAction = QAction(QIcon('exit.png'), '&Exit', self)

        exitAction.setShortcut('Ctrl+Q')

        exitAction.setStatusTip('Exit Application')

        exitAction.triggered.connect(qApp.quit)


        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')

        editMenu = menubar.addMenu('&Eidt')

        fileMenu.addAction(exitAction)


        self.toobar = self.addToolBar('Exit')
        
        self.toobar.addAction(exitAction)


        self.statusBar().showMessage('Ready')


        self.setGeometry(300, 300,350,350)

        self.setWindowTitle('Main window')

        self.show()


    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:

            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
