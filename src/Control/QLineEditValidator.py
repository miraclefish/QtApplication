import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QMainWindow, QGridLayout, QPushButton, QToolTip, QLabel, QDialog, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):

    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("校验器")

        formlayout = QFormLayout(self)

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formlayout.addRow("整数类型", intLineEdit)
        formlayout.addRow("浮点类型", doubleLineEdit)
        formlayout.addRow("数字和字母", validatorLineEdit)

        intLineEdit.setPlaceholderText("整数类型")
        doubleLineEdit.setPlaceholderText("浮点类型")
        validatorLineEdit.setPlaceholderText("数字和字母")

        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        floatValidator = QDoubleValidator(self)
        floatValidator.setRange(-360, 360)
        floatValidator.setNotation(QDoubleValidator.StandardNotation)
        floatValidator.setDecimals(2)

        reg = QRegExp('[a-zA-z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(floatValidator)
        validatorLineEdit.setValidator(validator)




if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()

    sys.exit(app.exec_())