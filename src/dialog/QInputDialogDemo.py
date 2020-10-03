'''
QInputDialog

输入对话框

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QInputDialogDemo(QWidget):

    def __init__(self):
        super(QInputDialogDemo,self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QInputDialog控件演示")

        layout = QFormLayout(self)

        self.b1 = QPushButton('获取列表中的选项')
        self.b1.clicked.connect(self.getItem)
        self.l1 = QLineEdit()
        layout.addRow(self.b1, self.l1)

        self.b2 = QPushButton('获取字符串')
        self.b2.clicked.connect(self.getText)
        self.l2 = QLineEdit()
        layout.addRow(self.b2, self.l2)

        self.b3 = QPushButton('获取整数')
        self.b3.clicked.connect(self.getInt)
        self.l3 = QLineEdit()
        layout.addRow(self.b3, self.l3)

        # self.xx = QInputDialog()
    def getItem(self):
        items = ('C','C++', 'Ruby', 'Python', 'Java')
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if ok and item:
            self.l1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, '文本输入框', '输入姓名')
        if ok and text:
            self.l2.setText(text)
        
    def getInt(self):
        num, ok = QInputDialog.getInt(self, '整数输入框', '输入数字')
        if ok and num:
            self.l3.setText(str(num))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()

    sys.exit(app.exec_())