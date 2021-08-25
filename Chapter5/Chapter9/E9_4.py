def exercise(Archive):
    try:    
        fHande = open(Archive,'r')
        fDict = dict()
        biggerDictName = ['oi']
        biggerDictValue = 0
        for line in fHande:
            if not line.startswith('From ') or len(line) == 0: continue
            weekday = line.split()[1]
            fDict[weekday] = fDict.get(weekday,0) + 1
        for key in fDict:
            if fDict[key] > biggerDictValue:
                biggerDictName[0] = key 
                biggerDictValue = fDict[key]
        print("%s %d"%(biggerDictName[0],biggerDictValue))
    except:
        print('file don\'t finded: %s'%Archive)

exercise(input('Enter a file name: ')) 