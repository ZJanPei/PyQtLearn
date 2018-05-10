import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QCheckBox, QApplication, QSlider, QCalendarWidget, QLabel, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QDate, QBasicTimer
from PyQt5.QtGui import QColor

class Example(QWidget):
    ''' '''
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ''' '''

        checkBox = QCheckBox('Show title', self)
        checkBox.move(20, 20)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.changeTitle)

        self.color = QColor(0, 0, 0)

        redBtn = QPushButton('Red', self)
        redBtn.setCheckable(True)
        redBtn.move(20, 60)
        redslider = QSlider(Qt.Horizontal, self)
        redslider.setFocusPolicy(Qt.NoFocus)
        redslider.setGeometry(100, 60,100,20)
        redBtn.clicked[bool].connect(self.setColor)
        redslider.valueChanged[int].connect(self.changeRedValue)

        greenBtn = QPushButton('Green', self)
        greenBtn.setCheckable(True)
        greenBtn.move(20, 100)
        greenslider = QSlider(Qt.Horizontal, self)
        greenslider.setFocusPolicy(Qt.NoFocus)
        greenslider.setGeometry(100, 100,100,20)
        greenBtn.clicked[bool].connect(self.setColor)
        greenslider.valueChanged[int].connect(self.changeGreenValue)

        blueBtn = QPushButton('Blue', self)
        blueBtn.setCheckable(True)
        blueBtn.move(20, 140)
        blueslider = QSlider(Qt.Horizontal, self)
        blueslider.setFocusPolicy(Qt.NoFocus)
        blueslider.setGeometry(100, 140,100,20)
        blueBtn.clicked[bool].connect(self.setColor)
        blueslider.valueChanged[int].connect(self.changeBlueValue)

        
        calinder = QCalendarWidget(self)
        calinder.setGridVisible(True)
        calinder.move(160, 200)
        calinder.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = calinder.selectedDate()
        self.label.setText(date.toString())
        self.label.move(20,200)

        self.frame = QFrame(self)
        self.frame.setGeometry(350,60, 100, 100)
        self.frame.setStyleSheet('QWidget {background-color: %s}'% self.color.name()) 

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 450, 500, 20)

        self.pBtn = QPushButton('Start', self)
        self.pBtn.move(20, 400)
        self.pBtn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300,300,600,500)
        self.setWindowTitle('控件示例')
        self.show()

    def setColor(self, pressed):
        ''' '''
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.color.setRed(val)
        elif source.text() == 'Green':
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)

        self.frame.setStyleSheet('QWidget {background-color: %s}'% self.color.name()) 

    def changeRedValue(self, value):
        ''' '''
        colorvalue = (value+1)*255//100

        self.color.setRed(colorvalue)

        self.frame.setStyleSheet('QWidget {background-color: %s}'% self.color.name()) 

    def changeGreenValue(self, value):
        ''' '''
        colorvalue = (value+1)*255//100

        self.color.setGreen(colorvalue)

        self.frame.setStyleSheet('QWidget {background-color: %s}'% self.color.name()) 
    def changeBlueValue(self, value):
        ''' '''
        colorvalue = (value+1)*255//100

        self.color.setBlue(colorvalue)

        self.frame.setStyleSheet('QWidget {background-color: %s}'% self.color.name()) 

    def changeTitle(self, state):
        ''' '''
        if state == Qt.Checked:
            self.setWindowTitle('控件选择')
        else:
            self.setWindowTitle('控件未选择')
            

    def showDate(self, date):
        ''' '''
        self.label.setText(date.toString())

    def doAction(self):
        ''' '''
        if self.timer.isActive():
            self.timer.stop()
            self.pBtn.setText('Start')
        else:
            self.timer.start(100, self)
            self.step = 0
            self.pBtn.setText('Stop')

    def timerEvent(self, event):
        ''' '''
        if self.step >= 100:
            self.timer.stop()
            self.pBtn.setText('Start')
            return
        self.step += 1
        self.pbar.setValue(self.step)

    def keyPressEvent(self, event):
        '''重写事件处理器函数 '''

        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
