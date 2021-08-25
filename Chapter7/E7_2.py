file = input('Enter file name: ')

def takeValues(archive):
    acumulator = 0
    countLine = 0
    for line in archive:
        if line.startswith('X-DSPAM-Confidence:'):
            acumulator += float(line[line.find(':')+1:])
            countLine += 1
    print('Average Span Confidence: %f'%(acumulator/countLine))
try:
    fHandle = open(file)
    takeValues(fHandle)
except:
    print('archive don\'t finded')
