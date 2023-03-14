# FTC Scouting Logger

## Install Instructions

1. Make sure pip is installed on your computer, if not here are some
   instructions (https://pip.pypa.io/en/stable/installation/)
2. Make sure tkinter is installed on your computer, if not here are some
   instructions (https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
3. Install python3, instructions (https://www.python.org/downloads/)
4. Clone or fork this repository
5. Done

### How to use

- The only file you need to change is questions.txt or config.txt, the format is **'question':type** for type, you can use type for a
  typing question, draw for a drawing question, or yn for a yes no question
- It will automatically store the questions and answers in log.txt, if you want to change the name, change it in
  config.txt under the name fileToOpen
- Width and height are the width and height of the window, you can change it in config.txt, it uses text digits so it might be a weird number
- You will need to run logger.py to start the program, it will auto generate all the information and questions