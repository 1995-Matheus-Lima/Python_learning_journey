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
        print("max: %.2f\nmin: %.2f"%(max(arrayNums),min(arrayNums)))
    else:
        print('Done!')    
        
sumAverage()