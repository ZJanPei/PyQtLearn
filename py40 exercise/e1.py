import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    print(sys.argv)

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(600, 600)

    w.move(100, 100);

    w.setWindowTitle("E1")

    w.show()

    sys.exit(app.exec_())
