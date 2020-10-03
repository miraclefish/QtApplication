'''
QFontDialog

字体对话框

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QFontDialogDemo(QWidget):

    def __init__(self):
        super(QFontDialogDemo,self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Font Dialog例子")

        layout = QVBoxLayout(self)
        self.fontbutton = QPushButton('选择字体')
        self.fontbutton.clicked.connect(self.getFont)
        layout.addWidget(self.fontbutton)

        self.fontlabel = QLabel('Hello,测试字体样例')
        layout.addWidget(self.fontlabel)
        
    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontlabel.setFont(font)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()

    sys.exit(app.exec_())