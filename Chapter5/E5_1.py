def sumAverage():
    arrayNums = []
    
    while True:
        x = input('Enter a Number')
        if x == "Done" or x == 'done':
            break
        else:
            try:
                y = float(x)
                arrayNums.append(y)
                print(arrayNums)
            except:
                print('Invalid value')
    if len(arrayNums) != 0:
        print("total: %.2f\ncount: %d\nAverage: %.2f"%(sum(arrayNums),len(arrayNums),sum(arrayNums)/len(arrayNums)))
    else:
        print('Done!')    
        
sumAverage()