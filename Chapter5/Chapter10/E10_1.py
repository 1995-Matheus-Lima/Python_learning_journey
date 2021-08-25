def mostCommom(archive):
    try:
        fhand = open(archive)
        dictionary = dict()
        for line in fhand:
            if not line.startswith("From ") or len(line) == 0: continue
            dictionary[line.split()[1]] = dictionary.get(line.split()[1],0)+1
        addressList = list()
        for address, value in dictionary.items():
            addressList.append((value,address))
        addressList.sort(reverse = True)
        print("%s %d"%(addressList[0][1],addressList[0][0]))
    except:
        print('file don\'t finded: %s'%archive)

mostCommom(input('Enter a file name:  '))