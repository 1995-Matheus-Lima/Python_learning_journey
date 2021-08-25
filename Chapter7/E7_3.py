file = input('Enter file name: ')

def countLine(archive):
  
    countLine = 0
    for line in archive:
        if line.startswith('Subject'):
            countLine += 1
    print('There\'s %d subjects lines in %s'%(countLine, file))
try:
    fHandle = open(file)
    countLine(fHandle)
except:
    if file == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        print('archive don\'t finded: %s'%file)
