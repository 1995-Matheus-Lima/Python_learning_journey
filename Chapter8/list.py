myList = ['claudete','viny','tata','tom','alaninha','emily','eu']
print(myList)
myList[-1] = 'matheus'
print(myList)
for item in myList:
    myList[myList.index(item)] = item.capitalize()
print(myList)

