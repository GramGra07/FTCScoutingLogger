import re
import datetime
import os
import tkinter as tk
from tkinter import *
import PIL
from PIL import Image
from PIL import Image, ImageDraw, ImageTk

global file2Open
global width
global height
global color1
global color2
global title
global finalMessage
global font
config = open("editableFiles/config.txt", "r")
lines = config.readlines()
count = 0
for line in lines:
  line = line.replace("\n", "")
  if count % 2 == 0:
    count += 1
    continue
  if count % 2 == 1:
    if "title" in lines[count - 1]:
      title = lines[count]
      title = title.replace("\n", "")
    if "font" in lines[count - 1]:
      font = lines[count]
      font = font.replace("\n", "")
    if "fileToOpen" in lines[count - 1]:
      file2Open = lines[count]
      file2Open = file2Open.replace("\n", "")
    elif "width" in lines[count - 1]:
      width = int(lines[count])
    elif "height" in lines[count - 1]:
      height = int(lines[count])
    elif "color1" in lines[count - 1]:
      color1 = lines[count]
      color1 = color1.replace("\n", "")
    elif "color2" in lines[count - 1]:
      color2 = lines[count]
      color2 = color2.replace("\n", "")
    elif "finalMessage" in lines[count - 1]:
      finalMessage = lines[count]
      finalMessage = finalMessage.replace("\n", "")
    count += 1
config.close()

global cvHeight
global cvWidth
textSize = 45
cv = open("utilDir/constraints.txt", "r")
lines2 = cv.readlines()
count = 0
for line in lines2:
  line = line.replace("\n", "")
  if count % 2 == 0:
    count += 1
    continue
  if count % 2 == 1:
    if "height" in lines2[count - 1]:
      cvHeight = int(lines2[count])
    elif "width" in lines2[count - 1]:
      cvWidth = int(lines2[count])
    count += 1
cv.close()

c = "blue"
window = tk.Tk()
window.title(title)


def log(file2Open, question, answer):
  ct = str(str(datetime.datetime.now()))
  c, sep, tail = ct.partition('.')
  print(c, question, answer)
  l = open(str(file2Open), "a")
  txt = c + " " + question + " " + answer + '\n'
  l.write(txt)
  l.close()


qtxt = open("editableFiles/questions.txt", "r")
Lines = qtxt.readlines()
count = 0
qs = {}
for line in Lines:
  count += 1
  m = re.match(r"\'(.*)\':(\S+)", line)
  qs[str(m.group(1))] = str(m.group(2))
questions = list(qs)
qtxt.close()
done = False
steps = []
for q in range(len(questions)):
  steps.append(q)
steps.append(len(questions))

counter = 0


def question(q = 0):
  global counter
  counter += 1
  global myVars
  myVars = vars()
  global quest
  quest = questions[q]
  if list(qs.values())[q] == 'type':
    myVars["b" + str(counter)] = (
      tk.Button(text="Done", foreground=color1, width=width, height=3, font=(font, textSize), master=window))
    myVars["b" + str(counter)].bind("<Button-1>", donePressed)
    myVars["l" + str(counter)] = tk.Label(text=quest, foreground=color1, background=color2, width=width,
                                          height=int(height / 2), font=(font, textSize),
                                          master=window)
    myVars["e" + str(counter)] = tk.Entry(width=width, fg=color1, bg=color2, master=window,
                                          font=(font, textSize), justify=tk.CENTER)

    myVars["l" + str(counter)].pack(side=tk.TOP, expand=True, padx=5, pady=5)
    myVars["e" + str(counter)].pack(side=tk.TOP, expand=True, padx=5, pady=5)
    myVars["b" + str(counter)].pack(side=tk.TOP, expand=True, padx=5, pady=5)
  elif list(qs.values())[q] == 'yn':
    myVars["l" + str(counter)] = tk.Label(text=quest, foreground=color1, background=color2, width=int(width * 2),
                                          height=int(height / 3), font=(font, textSize), master=window)
    myVars["b" + str(counter)] = tk.Button(text="Yes", width=int(width / 2), height=int(height / 3), fg=color2,
                                           master=window, font=(font, int(textSize / 2)))
    myVars["b" + str(counter)].bind("<Button-1>", yesPressed)
    myVars["b" + str(counter + 1)] = tk.Button(text="No", width=int(width / 2), height=int(height / 3), fg=color2,
                                               master=window, font=(font, int(textSize / 2)))
    myVars["b" + str(counter + 1)].bind("<Button-1>", noPressed)

    myVars["l" + str(counter)].pack(side=tk.TOP, expand=True, padx=5, pady=5)
    myVars["b" + str(counter)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    myVars["b" + str(counter + 1)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)
  elif list(qs.values())[q] == 'draw':
    # draw
    myVars["cv" + str(counter)] = Canvas(window, width=cvWidth, height=cvHeight, bg='white')
    myVars["img" + str(counter)] = ImageTk.PhotoImage(Image.open("utilDir/field 2.png"))
    myVars["cv" + str(counter)].create_image(0, 0, anchor=NW, image=myVars["img" + str(counter)])
    myVars["image1" + str(counter)] = PIL.Image.new('RGB', (640, 480), 'white')
    myVars["draw" + str(counter)] = ImageDraw.Draw(myVars["image1" + str(counter)])
    myVars["cv" + str(counter)].bind('<1>', activate_paint)
    myVars["b" + str(counter)] = tk.Button(text="Blue", width=10, height=10, fg="Blue", bg="blue", master=window)
    myVars["b" + str(counter)].bind("<Button-1>", turnBlue)
    myVars["b" + str(counter + 1)] = tk.Button(text="Red", width=10, height=10, fg="Red", bg="red", master=window)
    myVars["b" + str(counter + 1)].bind("<Button-1>", turnRed)
    myVars["clear" + str(counter)] = Button(text="clear", width=10, height=10, fg="black", bg="white",
                                            master=window)
    myVars["clear" + str(counter)].bind("<Button-1>", clearAll)
    myVars["btnSave" + str(counter)] = Button(text="save", command=save)

    myVars["cv" + str(counter)].pack(expand=True)
    myVars["b" + str(counter)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    myVars["b" + str(counter + 1)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    myVars["clear" + str(counter)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    myVars["btnSave" + str(counter)].pack(side=tk.LEFT, expand=True, padx=5, pady=5)

  if "end" in quest:
    finished = tk.Label(text=finalMessage, foreground=color1, background=color2,
                        width=int(width * 2),
                        height=int(height), font=(font, textSize - 20), master=window)
    finished.pack(side=tk.TOP, expand=True, padx=5, pady=5)
  window.mainloop()


def donePressed(event):
  global teamNumber
  global teamName
  if ("team number" in quest):
    teamNumber = str(myVars["e" + str(counter)].get())
  if ("team name" in quest):
    teamName = str(myVars["e" + str(counter)].get())
  log(file2Open, quest, str(myVars["e" + str(counter)].get()))
  myVars["l" + str(counter)].pack_forget()
  myVars["e" + str(counter)].pack_forget()
  myVars["b" + str(counter)].pack_forget()
  if counter < count:
    question(counter)


def yesPressed(event):
  log(file2Open, quest, 'yes')
  myVars["l" + str(counter)].pack_forget()
  myVars["b" + str(counter)].pack_forget()
  myVars["b" + str(counter + 1)].pack_forget()
  if (counter < count):
    question(counter)


def noPressed(event):
  log(file2Open, quest, 'no')
  myVars["l" + str(counter)].pack_forget()
  myVars["b" + str(counter)].pack_forget()
  myVars["b" + str(counter + 1)].pack_forget()
  if (counter < count):
    question(counter)


def save():
  global filepath
  filepath = "pictures/"
  global filename
  filename = f'{teamNumber , teamName}'
  global fileTag
  fileTag = ".png"
  filename += fileTag

  myVars["image1" + str(counter)].save(filepath + "transPar" + filename)

  img = Image.open(filepath + "transPar" + filename)
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = list()
  for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
      newData.append((255, 255, 255, 0))
    else:
      newData.append(item)
  img.putdata(newData)
  img.save(filepath + "transPar2" + filename)

  background = Image.open("utilDir/field 2.png")
  foreground = Image.open(filepath + "transPar2" + filename)
  background.paste(foreground, (0, 0), foreground)
  savename = filepath + quest + "_" + filename
  background.save(savename)
  os.remove(filepath + "transPar" + filename)
  os.remove(filepath + "transPar2" + filename)

  log(file2Open, quest, filename + " saved")

  myVars["cv" + str(counter)].pack_forget()
  myVars["b" + str(counter)].pack_forget()
  myVars["b" + str(counter + 1)].pack_forget()
  myVars["clear" + str(counter)].pack_forget()
  myVars["btnSave" + str(counter)].pack_forget()
  if (counter < count):
    question(counter)


def activate_paint(e):
  global lastx, lasty
  myVars["cv" + str(counter)].bind('<B1-Motion>', paint)
  lastx, lasty = e.x, e.y


def paint(e):
  global lastx, lasty
  x, y = e.x, e.y
  myVars["cv" + str(counter)].create_line((lastx, lasty, x, y), width=3, fill=c)
  myVars["draw" + str(counter)].line((lastx, lasty, x, y), fill='black', width=1)
  lastx, lasty = x, y


def turnRed(e):
  global c
  c = "red"


def turnBlue(e):
  global c
  c = "blue"


def clearAll(e):
  myVars["cv" + str(counter)].delete('all')
  myVars["cv" + str(counter)].create_image(0, 0, anchor=NW, image=myVars["img" + str(counter)])
