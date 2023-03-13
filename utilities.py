import re
import datetime


def log(file2Open, question, answer):
    l = open(str(file2Open), "a")
    txt = question + answer + '\n'
    l.write(txt)
    l.close()
    ct = str(str(datetime.datetime.now()))
    c, sep, tail = ct.partition('.')
    print(c, question, answer)


file = open("fileToOpen.txt", "r")
global file2Open
file2Open = file.read()
file.close()
qtxt = open("questions.txt", "r")
Lines = qtxt.readlines()
count = 0
qs = {}
for line in Lines:
    count += 1
    m = re.match(r"\'(.*)\':(\S+)", line)
    qs[str(m.group(1))] = str(m.group(2))
questions = list(qs)
qtxt.close()
width = 720
height = 720
done = False
steps = []
for q in range(len(questions)):
    steps.append(q)
steps.append(len(questions))

def question(q):
    q -= 1
    if (list(qs.values())[q] == 'type'):
        pass
    if (list(qs.values())[q] == 'yn'):
        pass
    elif (list(qs.values())[q] == 'draw'):
        pass
