from PyQt5.QtWidgets import QMainWindow
from ui_Login import Ui_Login

class Login(QMainWindow, Ui_Login):
    '''登录界面'''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OKpushButton.clicked.connect(self.OKClicked)
        self.CancelpushButton.clicked.connect(self.CancelClicked)

        self.show()

    def OKClicked(self):
        '''处理确定按钮按下功能'''

        print(self.OKpushButton.text())

    def CancelClicked(self):
        '''处理取消按钮按下功能'''

        self.close()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())
