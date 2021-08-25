import re

def grep(regularExpression,ArchiveNAme):
    try:
        fhandle = open(ArchiveNAme,'r')
        thislist = list()
        for line in fhandle:
            x = re.findall(regularExpression,line)
            if len(x) > 0:
                thislist += x
        for finded in thislist:
            print(finded)
    except:
        print('invalid input, please check it!')
x = input('Enter with a regular expression: ')
y = input('Enter a file name: ')
grep(x,y)
