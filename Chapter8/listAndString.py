# we can separate a string in a list lettler by letter using list
myString = 'Matheus'
myList = list(myString)
print(myList)

# we can break string in a specifics points using split
breakString = 'i have a green duck'
breaked = breakString.split()
breaked2 = breakString.split('a')
print(breaked) #['i', 'have', 'a', 'green', 'duck']
print(breaked2) # ['i h', 've ', ' green duck']

#join is the inverse of the split
newBreaked = ' '.join(breaked)
newBreaked2 = 'a'.join(breaked2)
print(newBreaked)
print(newBreaked2)