def mostCommom(archive):
    try:
        fhand = open(archive)
        dictionary = dict()
        for line in fhand:
            if not line.startswith("From ") or len(line) == 0: continue
            dictionary[(line.split()[5]).split(':')[0]] = dictionary.get((line.split()[5]).split(':')[0],0) +1  
        print(dictionary)
        hourList = list()
        for hour,value in dictionary.items():
            hourList.append((hour,value))
        hourList.sort()
        for item in hourList:
            print('%s %d'%item)
    except:
        print('file don\'t finded: %s'%archive)

mostCommom(input('Enter a file name:  '))