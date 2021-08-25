myList = ['a', 'b', 'c', 'd', 'e', 'f']
mySecondList = ['g']
myThirdyList = ['h', 'i', 'j']
# append add a new element in the end of a list
myList.append(mySecondList[0])
print(myList)
print(mySecondList)
#extend takes a list as a argument and appends all of the elements
myList.extend(myThirdyList)
print(myList)
#sort arranges the elements of the list from low to high
strangeList = ['h','a','g','b','m']
#strangeList = strangeList.sort()    it returns none
strangeList.sort()
print(strangeList)

# most of list methods returns void, so we may get dessapointed sometimes if we use it in a wrong way
# as in the example above strangeList = strangeList.sor()  the second party will return void,  so
# when we print this, we will see none um our screen
