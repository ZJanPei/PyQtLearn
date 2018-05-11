from PyQt5.QtWidgets import QMainWindow
from ui_Main import Ui_Main
from login import Login

class Main(QMainWindow, Ui_Main):
    '''主界面'''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.LoginpushButton.clicked.connect(self.LoginClicked)

        self.show()

    def LoginClicked(self):
        '''处理登录按键，弹出登录对话框'''

        self.login = Login()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
