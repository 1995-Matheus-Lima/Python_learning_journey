str = 'X-DSPAM-Confidence: 0.8475'
indexColon = str.find(':')
newStr = str[indexColon+1:]
newNumber = float(newStr)
print(newNumber)
print(type(newNumber))