import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QMainWindow, QGridLayout, QPushButton, QToolTip, QLabel, QDialog, QLineEdit
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt

class QLineEditEcho(QWidget):

    def __init__(self):
        super(QLineEditEcho, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入的回显模式")

        formlayout = QFormLayout(self)

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoLineEdit = QLineEdit()

        formlayout.addRow("Normal", normalLineEdit)
        formlayout.addRow("NoEcho", noEchoLineEdit)
        formlayout.addRow("password", passwordLineEdit)
        formlayout.addRow("passwordEcho", passwordEchoLineEdit)

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoLineEdit.setPlaceholderText("PasswordEcho")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QLineEditEcho()
    main.show()

    sys.exit(app.exec_())