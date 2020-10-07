'''
像素点绘制正弦曲线

drawPoint(x,y)

'''


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont
import sys
import math

class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.setWindowTitle('绘制正弦曲线')
        self.resize(300,200)
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i/1000) + size.width()/2.0
            y = -50 * math.sin((x - size.width()/2.0) * math.pi/50) + size.height()/2.0
            painter.drawPoint(x, y)

        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = DrawPoints()
    main.show()

    sys.exit(app.exec_())