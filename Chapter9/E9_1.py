fhand = open('words.txt', 'r')
fDict = {}
for line in fhand:
    lineArray = line.rstrip().split()
    for word in lineArray:
        fDict[word] = lineArray.index(word)
print(fDict)
