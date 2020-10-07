'''
绘制不同直线

drawLine(x1, y1, x2, y2)

'''


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont,QPen
import sys
import math

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.setWindowTitle('设置Pen的样式')
        self.resize(300,200)
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,8,5,8])
        painter.setPen(pen)
        painter.drawLine(20,120,250,120)


        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()

    sys.exit(app.exec_())