from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup

app = QApplication([])
win = QWidget()
win.setWindowTitle("Radio")
win.move (300,300)
win.resize(800,800)
win.show()

line = QVBoxLayout()
button = QPushButton()
line.addWidget(button, alignment=Qt.AlignCenter)
win.setLayout(line)
radio1 = QRadioButton("1")
radio1.setChecked(True)
radio2 = QRadioButton("2")
radio3 = QRadioButton("3")

button_Group = QButtonGroup()
button_Group.addButton(radio1, id = 1)
button_Group.addButton(radio2, id = 2)
button_Group.addButton(radio3, id = 3)
line.addWidget(radio1)
line.addWidget(radio2)
line.addWidget(radio3)


title = QLabel()
line.addWidget(title, alignment=Qt.AlignCenter)
win.setLayout(line)


def radiocheck():
    title.setText("You have selected button number" , button_Group.checkedId()))

button.clicked.connect(radiocheck)









app.exec_()