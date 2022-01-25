from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class UIForm(QMainWindow):
    def __init__(self):
        super(UIForm,self).__init__()
        uic.loadUi('main.ui',self)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=UIForm()
    window.show()
    app.exec_()