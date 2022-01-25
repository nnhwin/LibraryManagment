from PyQt5.QtWidgets import QApplication,QWidget
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Hello QWidget"
        self.left=10
        self.top=10
        self.width=400
        self.height=250


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    ex.show()
    sys.exit(app.exec_())
