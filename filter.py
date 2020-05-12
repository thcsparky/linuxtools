import os

dir = os.getcwd()
a = os.scandir(dir)
filesnow = ""
for x in a:
    if x.is_dir() == True:
        pass
    else:
        filesnow += x.path + '\n'

        a = os.system('file ' + x.path + '>> ./files.txt')
        weird = str(type(a))
        weird = weird.replace("<class 'int'>", "")

o = open(os.getcwd() + '/files.txt')
files = o.read()
o.close()

inp = input('what type\n').rstrip()

for x in files.splitlines():
    if x.find(':') > -1 and x.find(inp) > -1:
        print(x.split(':')[0])
quit()
