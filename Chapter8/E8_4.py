fhand = open('romeo.txt','r')
words = []
for line in fhand:
    x = line.split()
    for word in x:
        if not word in words:
            words.append(word)
words.sort()
print(words)