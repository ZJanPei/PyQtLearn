import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    ''' '''
    def __init__(self):
        ''' '''
        super().__init__()

        self.initUI()

    def initUI(self):
        ''' '''
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        
        self.setGeometry(300, 300,300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
