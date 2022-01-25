from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class LoginCheck(QDialog):
    def __init__(self):
        super(LoginCheck, self).__init__()
        uic.loadUi('loginform.ui', self)
        self.setMyStyle()
        self.loginbut.clicked.connect(self.LoginProcess)
        self.signupbut.clicked.connect(self.SignupProcess)

    def LoginProcess(self):
        usr = self.usrTxt.toPlainText().strip()
        pwd = self.pwdTxt.text().strip()
        print(f"user {usr}")
        print(f"password {pwd}")


    def SignupProcess(self):
        print('in signup')

    def setMyStyle(self):
            self.loginlogo.setStyleSheet("background-image:url(oo.jpg);\n"
                                     "width:100%;\n"
                                     "height:100%;")
            self.loginlogo.setScaledContents(True);
            self.loginlogo.setPixmap(QPixmap("oo.jpg"))
            self.loginbut.setStyleSheet("QPushButton { background-color:#F5CBA7;"
                                          "border-width: 2px;border-radius: 10px;}"
                                          "QPushButton:pressed { background-color: #185189226}"
                                          "QPushButton:hover {background-color: #FDEDEC;}")

            self.signupbut.setStyleSheet("QPushButton { background-color:#F5CBA7;"
                                        "border-width: 2px;border-radius: 10px;}"
                                        "QPushButton:pressed { background-color: #185189226}"
                                        "QPushButton:hover {background-color: #FDEDEC;}")


if __name__=="__main__":
    app=QApplication(sys.argv)
    login=LoginCheck()
    login.show()
    sys.exit(app.exec_())

