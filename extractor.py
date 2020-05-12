import os
import re

dir = os.getcwd() + '/'

thiss = os.scandir(dir)
liststuff = []
for x in thiss:
    if x.is_file() == True:
        liststuff.append(x)
num = 1
for x in liststuff:
    print(x.path)
    num += 1

inp =  input('What file? use grep -r > file.txt or whatever for more easier search... \n\n').rstrip()

try:
    fileio = open(dir + inp)
    contents = fileio.read()
    inp3 = input('Enter regex: \n').rstrip()
    rere = re.compile(inp3)

    o = rere.findall(contents)
    for x in o:
        print(x)
    quit()
except:
    pass
