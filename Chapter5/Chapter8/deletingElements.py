myList = ['a','b','b','c','d']
# Pop is to be used when you know  the index of the element that you would like to remove from a list
print(myList)
myList.pop(1)
print(myList)
# pop modify the list and returns the elements that was removed, if you don't put the index you will
#remove and return the last element of the list!
removedElement = myList.pop(-1)
print(myList)
print(removedElement)

# if you don't know the index of the element but know which element, you can use remove
myList.remove('c')
print(myList)
# the return value from remove is none

# to remove more than one element we can use del with slice
del(myList[1:])
print(myList)
