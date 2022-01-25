import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ButtonEventeg(QDialog):

   def showdialog(self):
      dlg = QDialog()
      b1 = QPushButton("ok",dlg)
      b1.move(50,50)
      dlg.setWindowTitle("Dialog")
      dlg.setWindowModality(Qt.ApplicationModal)
      dlg.exec_()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   w = ButtonEventeg()
   btn = QPushButton(w)
   btn.setText("Hello World!")
   btn.move(100, 50)
   btn.clicked.connect(w.showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())