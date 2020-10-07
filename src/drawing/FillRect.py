'''
用画刷填充区域


'''


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt,QRect,QPoint
from PyQt5.QtGui import QPainter,QColor,QFont,QPen,QPolygon,QImage,QBrush
import sys
import math

class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.setWindowTitle('填充区域')
        self.resize(300,600)
        

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,15,90,60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15,90,60)
        
        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(10,100,90,60)
  
        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(130,100,90,60)
        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = FillRect()
    main.show()

    sys.exit(app.exec_())