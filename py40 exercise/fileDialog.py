import sys
from PyQt5.QtWidgets import *
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
        self.textEdit  = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)


        self.setGeometry(300,300,500,300)
        self.setWindowTitle('FileDilog Example')
        self.show()

    def showDialog(self):
        ''' '''
        fdialog = QFileDialog()

        fname = fdialog.getOpenFileName(self, '选取文件', './', 'All Files(*);; Text Files (*.txt)')

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:

            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
