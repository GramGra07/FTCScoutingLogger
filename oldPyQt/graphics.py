from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import keyboard
import json
import re

file = open("../editableFiles/fileToOpen.txt", "r")
file2Open = file.read()
file.close()
qtxt = open("../editableFiles/questions.txt", "r")
Lines = qtxt.readlines()
count = 0
qs = {}
for line in Lines:
    count += 1
    m = re.match(r"\'(.*)\':(\S+)", line)
    qs[str(m.group(1))] = str(m.group(2))
questions = list(qs)
qtxt.close()

boo = 'No', 'Yes'
width = 720
height = 720
done = False
steps = []
for q in range(len(questions)):
    steps.append(q)
steps.append(len(questions))


class qa(QMainWindow):
    def __init__(self, i):
        super().__init__()
        layout = QVBoxLayout(self)
        self.resize(width, height)
        self.setWindowTitle("Scouting Log")
        self.q = ''
        self.question(i)

    def question(self, q):
        q -= 1
        if (list(qs.values())[q] == 'type'):
            self.typeQuestion(q)
        if (list(qs.values())[q] == 'yn'):
            self.ynButton(q)
        elif (list(qs.values())[q] == 'draw'):
            self.draw(q)

    def typeQuestion(self, q):
        d = 100
        self.q = questions[q]
        self.input = QLineEdit(questions[q])
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.setCentralWidget(self.input)
        self.dbutton = QPushButton('Done', self)
        self.dbutton.move(int(width / 3 + d / 2), int(height / 2))
        self.dbutton.setFixedHeight(d)
        self.dbutton.setFixedWidth(d)
        self.dbutton.setCheckable(True)
        self.dbutton.clicked.connect(self.doneClicked)

    def draw(self):
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(x1, y1, x2, y2)
        painter.end()
        self.dbutton = QPushButton('Done', self)
        self.dbutton.move(int(width / 3 + d / 2), int(height - 100))
        self.dbutton.setFixedHeight(d)
        self.dbutton.setFixedWidth(d)
        self.dbutton.setCheckable(True)
        self.dbutton.clicked.connect(self.doneClicked)
        self.label.setPixmap(canvas)

    def ynButton(self, q):

        reply = QMessageBox.question(self, questions[q],
                                     questions[q], QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        self.question = questions[q]
        if reply == QMessageBox.StandardButton.Yes:
            self.yesClicked()
        else:
            self.noClicked()

    def yesClicked(self):
        self.log(self.question, 'yes')
        self.deleteLater()

    def noClicked(self):
        self.log(self.question, 'no')
        self.deleteLater()

    def doneClicked(self):
        self.log('', self.input.text())
        steps.pop(0)
        self.deleteLater()

    def mousePressEvent(self, e):
        print("mousePressEvent")

    def log(self, question, answer):
        l = open(file2Open, "a")
        txt = question + answer + '\n'
        l.write(txt)
        l.close()
        print(question, answer)
