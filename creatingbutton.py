from PyQt5 import *
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

app = QApplication([])
win = QWidget()
win.setWindowTitle("Creating buttons")
win.move(400,400)
win.resize(800,800)
win.show()

line = QVBoxLayout()

button = QPushButton()
line.addWidget(button, alignment=Qt.AlignTop)
win.setLayout(line)


def showingtitle():
    title = QLabel("Hello, world") 
    line.addWidget(title,alignment=Qt.AlignCenter)
    win.setLayout(line)

button.clicked.connect(showingtitle)


app.exec_()
