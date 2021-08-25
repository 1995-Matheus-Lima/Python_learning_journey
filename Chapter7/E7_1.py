def linePrint(archive):
    for line in archive:
        print(line.rstrip().upper())


file = input('Enter the file\'s name: ' )

try:
    fHandle = open(file)
    linePrint(fHandle)
except:
    print('Archive don\'t finded: %s'%file)

