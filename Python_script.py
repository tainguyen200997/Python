# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5 import *

def dialog():
    mbox = QMessageBox()
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)           
    mbox.exec_()
def calculator():
	pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Guru99')
  
    label = QLabel(w)
    label.setText("Behold the Guru, Guru99")
    label.move(90,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Result')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(calculator)

    EditLine = QLineEdit(w)
    EditLine.move(70,90)
    EditLine.show()

    w.show()
    sys.exit(app.exec_())

