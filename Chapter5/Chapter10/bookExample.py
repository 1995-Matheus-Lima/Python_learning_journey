fhandle = open('words.txt')
text = []
for line in fhandle:
    text += line.split()
textList = list()
for word in text:
    textList.append((len(word),word))
print(textList)
print('\n')
textList.sort(reverse=True)
print(textList)

res = list()

for length, word in textList:
    res.append(word)
print('\n')
print(res)
