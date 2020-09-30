import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QToolTip, QLabel, QDialog, QLineEdit
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt

class QLabelBuddy(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")

        namelabel = QLabel('&Name', self)
        namelineEdit = QLineEdit(self)

        namelabel.setBuddy(namelineEdit)

        passwordlabel = QLabel('&Password', self)
        passwordEdit = QLineEdit(self)

        passwordlabel.setBuddy(passwordEdit)
        
        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(namelabel, 0, 0)
        mainLayout.addWidget(namelineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordlabel, 1, 0)
        mainLayout.addWidget(passwordEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())
