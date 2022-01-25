from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5 import QtWidgets,QtGui
class mainForm(QMainWindow):

    def __init__(self):
        super(mainForm,self).__init__()
        uic.loadUi('mainWindow.ui',self)
        self.setMyStyle()
        self.pushButton.clicked.connect(self.startProgram)

    def startProgram(self):
        try:
            print("here")

        except Exception as e:
            print(str(e))

    def setMyStyle(self):
        self.label.setStyleSheet("background-image:url(../img/school.jpg);\n"
                                   "width:100%;\n"
                                   "height:100%;")

        self.pushButton.setStyleSheet("QPushButton { background-color:#F5CBA7;"
                                           "border-width: 2px;border-radius: 10px;}"
                                           "QPushButton:pressed { background-color: #185189226}"
                                           "QPushButton:hover {background-color: #FDEDEC;}")

app=QApplication(sys.argv)
window=mainForm()
window.show()
app.exec_()