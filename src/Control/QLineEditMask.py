'''
用掩码限制QLineEdit控件的输入

'''


from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("用掩码限制QLineEdit控件的输入")

        formlayout = QFormLayout(self)

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH.HH.HH.HH.HH.HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formlayout.addRow('数字掩码',ipLineEdit)
        formlayout.addRow('Mac掩码',macLineEdit)
        formlayout.addRow('日期掩码',dateLineEdit)
        formlayout.addRow('许可证掩码',licenseLineEdit)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()

    sys.exit(app.exec_())
