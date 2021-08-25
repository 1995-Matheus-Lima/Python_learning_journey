import re
from typing import Counter 
def average(archive):
    try:
        fhandle = open(archive,'r')
        sum = 0
        Counter = 0
        for line in fhandle:
            x = re.findall('New Revision:(.*)' ,line)
            if len(x) > 0:
                sum += float(x[0])
                Counter += 1
        print(sum/Counter)
    except:
        print('file don\'t finded: %s'%archive)
average(input('Enter a file name: '))