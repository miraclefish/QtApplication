import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget, QPushButton

class QuitApplication(QMainWindow):

    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")

        # 添加 Button
        self.button1 = QPushButton("退出应用程序")
        self.button1.clicked.connect(self.onClick_Button)
        
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe = QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()

        app.quit()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())