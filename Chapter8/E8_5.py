from typing import Counter


def mailBox():
    x = input('Enter with the archive name: ')
    countFrom = 0 
    try:
        fhand = open(x,'r')
        for line in fhand:
            if len(line) == 0 or not line.startswith('From'): continue
            lineSplit = line.split()
            print(lineSplit[1])
            countFrom += 1
    except:
        print('Archive not finded: %s'%x)
    print('There were %d lines in the file with From as the first word'%countFrom)

mailBox()