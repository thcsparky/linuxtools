import os

dir = os.getcwd() + '/'
a = os.scandir(dir)
b = []
for x in a:
    if x.is_file() == True:
        b.append(x.path)

filestotal = []
listy = 0
for x in b:
    listy += 1
    print(str(listy) + '. ' + x + '\n')
    filestotal.append(x)

inp2 = input('File Number: \n').rstrip()
thefile = ''
try:
    thefile = filestotal[int(inp2) - 1]
except:
    print('Error Marking File..\n')
    print(thefile)

if len(thefile) > 0:
    fileio = open(thefile)
    fileinfo = fileio.read()
    fileinfo = fileinfo.splitlines()
    fileio.close()

    position = 0
    for x in fileinfo:
        position += 1
        position2 = 0
        for y in fileinfo:
            position2 += 1
            if position != position2 and x == y:
                print('Duplicate detected: ' + fileinfo[position2] + '\n')
                
                del fileinfo[position2]

    ##save and export
    bigstring = ''
    for x in fileinfo:
        bigstring += x + '/n'

    fileio = open(thefile, 'w')
    fileio.write(bigstring)
    fileio.close()
    print ('Killed Duplicates in: ' + thefile + '\n')
