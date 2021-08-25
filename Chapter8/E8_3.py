fhand = open('mbox-short.txt','r')
for line in fhand:
    if len(line) == 0 or not line.startswith("From"): continue
    lineList = line.split()
    try:
        print(lineList[2])
    except: continue