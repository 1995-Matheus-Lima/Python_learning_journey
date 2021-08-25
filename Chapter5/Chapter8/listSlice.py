myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[1:4]) # ['b', 'c', 'd']

# we can use slice to replace/change multiples values in the same time! 
myList[1:3] = ['banana','Caju']
print(myList) # ['a', 'banana', 'Caju', 'd', 'e', 'f']