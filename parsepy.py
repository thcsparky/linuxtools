import os

herez = os.getcwd() + '/'

thefile = input('file \n').rstrip()
theparse = input('split\n').rstrip()
thedirection = input('left/right\n').rstrip()
thequestion = input('Save? leave blank for standard output.. sort of\n').rstrip()
if len(thequestion) > 0:
    thequestion = herez + thequestion

thepossibleoutput = ''

thestream = open(thefile)
thetext = thestream.read()
thelines = thetext.splitlines()


for x in thelines:
    try:
        if thequestion == '':
            if thedirection == 'left':
                print(x.split(theparse)[0])
            elif thedirection == 'right':
                print(x.split(theparse)[1])
        else:
            if thedirection == 'left':
                thepossibleoutput += (x.split(theparse)[0]) + '\n'
            elif thedirection == 'right':
                thepossibleoutput += (x.split(theparse)[1]) + '\n'
    except:
        continue

if len(thepossibleoutput) > 0:
    a = open(thequestion, 'w')
    a.write(thepossibleoutput)
    a.close()


quit()
