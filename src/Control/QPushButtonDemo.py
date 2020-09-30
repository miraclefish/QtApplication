'''
QAbstractButton


QPushButton
AToolButton
QRadioButton
QCheckBox

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")


        layout = QVBoxLayout(self)

        self.button1 = QPushButton('第一个按钮')
        self.button1.setText("First Button1")
        self.button1.setC
        self.button1.toggle()

