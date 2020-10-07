'''
绘图API：绘制文本

1. 文本
2. 各种图形
3. 图像

QPainter

painter = QPainter()
painter.begin()
painter.drawText(...)
painter.end()

必须在paintEvent事件方法中绘制各种元素

'''


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont
import sys

class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.setWindowTitle('绘制文本')
        self.resize(300,200)
        self.text = "来办公室"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        print('500')
        painter.setPen(QColor(150,34,5))
        painter.setFont(QFont('SimSun', 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = DrawTextDemo()
    main.show()

    sys.exit(app.exec_())