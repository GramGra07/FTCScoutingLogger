# tutorial: https://www.youtube.com/watch?v=YXPyB4XeYLA
import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageTk
import utilities as util

c = "blue"
window = tk.Tk()


def donePressed(event):
    print(e.get())
    window.destroy()


def yesPressed(event):
    print('yes')
    window.destroy()


def noPressed(event):
    print('no')
    window.destroy()


def save():
    global image_number
    filename = f'image_{image_number}.png'  # image_number increments by 1 at every save
    image1.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=3, fill=c)
    draw.line((lastx, lasty, x, y), fill='black', width=1)
    lastx, lasty = x, y


def turnRed(e):
    global c
    c = "red"


def turnBlue(e):
    global c
    c = "blue"


def clearAll(e):
    cv.delete('all')
    cv.create_image(10, 10, anchor=NW, image=img)


width = 100
height = 20

# entry question
# b = tk.Button(text="Done", width=width, height=height, fg="black", bg="white", master=window)
# b.bind("<Button-1>", donePressed)
# l = tk.Label(text="hi", foreground="white", background="black", width=width, height=height,
#             master=window)
# e = tk.Entry(width=width, fg="black", bg="white", master=window)
# l.pack(side=tk.TOP, expand=True, padx=5, pady=5)
# e.pack(expand=True, padx=5, pady=5)
# b.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

# yes or no
# l = tk.Label(text="Yes or no", foreground="white", background="black", width=width, height=height)
# b = tk.Button(text="Yes", width=int(width/2), height=height, fg="black", bg="white", master=window)
# b.bind("<Button-1>", yesPressed)
# b2 = tk.Button(text="No", width=int(width/2), height=height, fg="black", bg="white", master=window)
# b2.bind("<Button-1>", noPressed)
# l.pack(side=tk.TOP, expand=True, padx=5, pady=5)
# b.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
# b2.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

# draw
lastx, lasty = None, None
image_number = 0
cv = Canvas(window, width=640, height=480, bg='white')
img = ImageTk.PhotoImage(Image.open("field.png"))
cv.create_image(10, 10, anchor=NW, image=img)
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
cv.bind('<1>', activate_paint)
b = tk.Button(text="Blue", width=10, height=10, fg="Blue", bg="blue", master=window)
b.bind("<Button-1>", turnBlue)
b2 = tk.Button(text="Red", width=10, height=10, fg="Red", bg="red", master=window)
b2.bind("<Button-1>", turnRed)
cv.pack(expand=YES, fill=BOTH)
b.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
b2.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
clear = Button(text="clear", width=10, height=10, fg="black", bg="white", master=window)
clear.bind("<Button-1>", clearAll)
clear.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
btn_save = Button(text="save", command=save)
btn_save.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

# legit setup for logging
util.setup()
file2Open = util.file2Open
util.log(file2Open, "test", '')

window.mainloop()  # run the window's main loop
