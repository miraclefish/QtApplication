'''
QSlideDemo

滑块控件

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QSlideDemo(QWidget):
    def __init__(self):
        super(QSlideDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("滑块控件演示")
        self.resize(300,700)

        layout = QVBoxLayout(self)

        self.label = QLabel("你好 PyQt5")
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        self.slider.setSingleStep(3)
        self.slider.setValue(18)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(6)
        self.slider.valueChanged.connect(self.valueChange)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setMinimum(10)
        self.slider1.setMaximum(60)
        self.slider1.setSingleStep(5)
        self.slider1.setValue(30)
        self.slider1.setTickPosition(QSlider.TicksLeft)
        self.slider1.setTickInterval(2)
        self.slider1.valueChanged.connect(self.valueChange)


        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)

    def valueChange(self):
        print('当前值：%s' %self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial', size))



if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QSlideDemo()
    main.show()

    sys.exit(app.exec_())