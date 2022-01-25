import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DialogClass(QDialog):
    def setupUI(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 208)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 191, 171))
        self.label.setStyleSheet( "width:100%;\n"
                                   "height:100%;")
        self.label.setText("Hello, QDialog")


if __name__=="__main__":
    app=QApplication(sys.argv)
    dia=QDialog()
    dia.setWindowTitle("QDIalog example")
    ui=DialogClass()
    ui.setupUI(dia)
    dia.show()
    sys.exit(app.exec_())