# QDesktopWidget

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        self.setWindowTitle("第一个主窗口应用")
        self.resize(400,300)
        self.center()

    def center(self):

        screen = QDesktopWidget().screenGeometry()

        size = self.geometry()
        newleft = (screen.width()-size.width())/2
        newtop = (screen.height()-size.height())/2
        self.move(newleft, newtop)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = CenterForm()
    main.show()

    sys.exit(app.exec_())