from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout

app = QApplication([])
win = QWidget()
win.setWindowTitle("My first application")
win.move(200,0)
win.resize(1600,1300)
win.show()


line = QHBoxLayout()
title = QLabel("Hello, world!")
line.addWidget(title, alignment=Qt.AlignTop)
win.setLayout(line)








app.exec_()
