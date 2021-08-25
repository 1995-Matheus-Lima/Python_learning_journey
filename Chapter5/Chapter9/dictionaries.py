engTwoSp = dict() 
engTwoSp['one'] = 'uno'
engTwoSp['two'] = 'dos'
engTwoSp['three'] = 'tres'
print(engTwoSp)
# the method len works in dictionaries
print(len(engTwoSp))

# you can check with the operator "in" if there are some key on the dictionarie, 
# but it doesn't find values just keys
print('one' in engTwoSp)
print('uno' in engTwoSp)

# to check a value inside the dictionaries you can use the method value
values = engTwoSp.values()
print('uno' in values)


