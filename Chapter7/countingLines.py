fhandle = open('opening.txt')
inp = fhandle.read()
count = 0
print(inp)
fhandle = open('opening.txt')
for line in fhandle:
    count += 1
print('lines: %d'%count) 
