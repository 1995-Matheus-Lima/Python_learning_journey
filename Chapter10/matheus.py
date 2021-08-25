import string
name = 'matheus@!#$@#$%'
print(name)
for letter in name:
    if letter in string.punctuation:
        name = name.replace(letter,'')
print(name)
print(string.punctuation)