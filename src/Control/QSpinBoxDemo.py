'''
QSpinBoxDemo

计数器控件

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("计数器控件演示")

        self.resize(300,100)
        layout = QVBoxLayout(self)

        self.label = QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.valueChanged.connect(self.valueChange)
        layout.addWidget(self.sb)

    def valueChange(self):
        self.label.setText('当前值：'+str(self.sb.value()))




if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()

    sys.exit(app.exec_())