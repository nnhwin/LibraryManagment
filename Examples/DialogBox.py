from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Hello QWidget"
        #self.setGeometry(self.left,self.top,self.width,self.height)
        self.left=10
        self.top=10
        self.width=400
        self.height=250
        self.butt=QPushButton("Click here",self)
        self.butt.clicked.connect(self.dialogboxfun)

    def dialogboxfun(self):
        buttonReply = QMessageBox.question(self, 'Hello', "Do you like cookies?", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print("Yeah")
        else:
            print("Nah")


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    ex.show()
    sys.exit(app.exec_())
