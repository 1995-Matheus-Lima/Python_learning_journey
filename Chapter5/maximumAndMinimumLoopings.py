nums = [3, 42, 12, 8, 32, 66, 82]
largest = None
for intervar in nums:
    if largest == None or intervar > largest:
        largest = intervar
    print('this:%d   ;largest: %d'%(intervar,largest))

print('largest %d'%(largest))
