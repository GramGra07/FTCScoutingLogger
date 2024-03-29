# FTC Scouting Logger

## About

This is a completely customizable resource for FTC teams for pre-match scouting. There are many features you can tweak
to your liking and customize. To run it you will run the logger.py. All configuration options are in config.txt. Only
edit every other line otherwise it will not work. You can change every question in questions.txt, but make sure you
follow the same format as demonstrated. I recommend keeping team name and number otherwise it might throw an error while
saving any image.

## Features

- Completely customizable
- Saves all data to a log.txt file
- Saves all images to a folder called pictures
- Is able to accept typing, drawing, and yes no questions
- Can be customized through config.txt including:
    - Title
    - Log file (fileToOpen)
    - Width
    - Height
    - Font
    - Color1
    - Color2
    - Final message

## Install Instructions

### Mac

1. Make sure pip is installed on your computer, if not here are some
   instructions (https://pip.pypa.io/en/stable/installation/)
2. Make sure tkinter is installed on your computer, if not here are some
   instructions (https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
3. Install python3, instructions (https://www.python.org/downloads/)
4. Clone or fork this repository, GitHub Desktop is very helpful as well as VsCode

### Windows

1. Make sure pip is installed on your computer, if not here are some
   instructions (https://pip.pypa.io/en/stable/installation/)
2. Make sure tkinter is installed on your computer, if not here are some
   instructions (https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
3. Install python3, instructions (https://www.python.org/downloads/)
4. Clone or fork this repository

### Ipad

Coming soon

### Linux

Coming soon

### How to use

- The only file you need to change is questions.txt or config.txt, the format is **'question':type** for type, you can
  use type for a
  typing question, draw for a drawing question, or yn for a yes no question
- You must have a question for team number and name for the file to save correctly
- If you want an end message, put 'end':done at the end of questions.txt
- It will automatically store the questions and answers in log.txt, if you want to change the name, change it in
  config.txt under the name fileToOpen
- You will also be able to change the colors of the window, here is a link to all color options
  provided (http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html)
- You can also change the title of the window, change it in config.txt under the name title
- Width and height are the width and height of the window, you can change it in config.txt, it uses text digits, so it
  might be a weird number
- You will need to run logger.py to start the program, it will auto generate all the information and questions
- It is easier if you fullscreen the window at the beginning of the program as it will auto resize