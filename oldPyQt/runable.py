from oldPyQt.graphics import *
import re
import datetime

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
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

file = open("../editableFiles/fileToOpen.txt", "r")
file2Open = file.read()
file.close()
ct = datetime.datetime.now()
ct = str(ct)
c, sep, tail = ct.partition('.')
c += '\n'
l = open(file2Open, "a")
l.write(c)
l.close()
# start
app = QApplication(sys.argv)
for i in range(count):
    locals()[alphabet[i]] = qa(i + 1)
    locals()[alphabet[i]].show()
    app.exec()
# end
sys.exit()
