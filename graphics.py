from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import keyboard
import json
import re
file = open("fileToOpen.txt","r")
file2Open = file.read()
file.close()
qtxt = open("questions.txt","r")
Lines = qtxt.readlines()
count = 0
qs = {}
for line in Lines:
   count+=1
   m = re.match(r"\'(.*)\':(\S+)",line)
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
   def __init__(self,i):
      super().__init__()
      layout = QVBoxLayout(self)
      self.resize(width,height)
      self.setWindowTitle("Scouting Log")
      self.q = ''
      self.question(i)
   def question(self,q):
      q-=1
      if (list(qs.values())[q] == 'type'):
         self.typeQuestion(q)
      elif (list(qs.values())[q] == 'yn'):
         self.ynButton(q)
   def typeQuestion(self,q):
       d=100
       self.q = questions[q]
       self.input = QLineEdit(questions[q])
       self.layout = QVBoxLayout()
       self.layout.addWidget(self.input)
       self.setCentralWidget(self.input)
       self.dbutton = QPushButton('Done',self)
       self.dbutton.move(int(width/3+d/2),int(height/2))
       self.dbutton.setFixedHeight(d)
       self.dbutton.setFixedWidth(d)
       self.dbutton.setCheckable(True)
       self.dbutton.clicked.connect(self.doneClicked)
       
##   def yesNoButton(self,q):
##      d = 100
##      label = QLabel(questions[q])
##      self.q = questions[q]
##      layout = QVBoxLayout()
##   
##      ybutton = QPushButton(boo[0],self)
##      ybutton.move(int(width/4*(2)+d/2),int(height/2))
##      ybutton.setFixedHeight(d)
##      ybutton.setFixedWidth(d)
##      ybutton.setCheckable(True)
##      ybutton.clicked.connect(self.yesClicked)
##      
##      nbutton = QPushButton(boo[1],self)
##      nbutton.move(int(width/4*(1)+d/2),int(height/2))
##      nbutton.setFixedHeight(d)
##      nbutton.setFixedWidth(d)
##      nbutton.setCheckable(True)
##      nbutton.clicked.connect(self.noClicked)
##      layout.addWidget(ybutton)
##      layout.addWidget(nbutton)
##      layout.addWidget(label)
   def ynButton(self, q):

        reply = QMessageBox.question(self, questions[q],
                    questions[q], QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
##        dlg = QMessageBox(self)
##        dlg.setWindowTitle("I have a question!")
##        dlg.setText("This is a simple dialog")
##        button = dlg.exec()
##
##        if button == QMessageBox.StandardButton.No:
##            self.noClicked()
##        else:
##            self.yesClicked()
        self.question = questions[q]
        if reply == QMessageBox.StandardButton.Yes:
           self.yesClicked()
        else:
           self.noClicked()
   def yesClicked(self):
       self.log(self.question,'yes')
       self.deleteLater()
   def noClicked(self):
       self.log(self.question,'no')
       self.deleteLater()
   def doneClicked(self):
       self.log('',self.input.text())
       steps.pop(0)
       self.deleteLater()
   def log(self,question,answer):
       l = open(file2Open, "a")
       txt = question+answer+'\n'
       l.write(txt)
       l.close()
       print(question,answer)

