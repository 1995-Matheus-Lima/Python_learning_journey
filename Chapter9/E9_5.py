def exercise(Archive):
    try:    
        fHande = open(Archive,'r')
        fDict = dict()
        for line in fHande:
            if not line.startswith('From ') or len(line) == 0: continue
            weekday = line.split()[1]
            fDict[weekday[weekday.index('@')+1:]] = fDict.get(weekday[weekday.index('@')+1:],0) + 1
        print(fDict)
    except:
        print('file don\'t finded: %s'%Archive)

exercise(input('Enter a file name: ')) 