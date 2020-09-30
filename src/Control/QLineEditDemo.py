from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLineEdit控件综合案例")

        # 使用int校验器
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  #不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)

        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)

        formlayout = QFormLayout(self)

        formlayout.addRow('整数校验', edit1)
        formlayout.addRow('浮点数校验', edit2)
        formlayout.addRow('Input Mask', edit3)
        formlayout.addRow('文本变化',edit4)
        formlayout.addRow('密码',edit5)
        formlayout.addRow('只读',edit6)
    
    def textChanged(self, text):
        print('输入的内容'+text)
    
    def enterPress(self):
        print('已键入值')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()

    sys.exit(app.exec_())

