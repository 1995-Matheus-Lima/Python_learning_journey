import re
fhande = open('mbox-short.txt','r')
# \S means that the are searcing a substring that don't have whitespace in an especificy position
# s = ' From : 1995.matheus.lima@gmail.com  to: 1999.emily.mancilha@gmail.com   @2pm'
# lst = re.findall('\S+@\S+',s)
# print(lst)
# mailList = list()
# for line in fhande:
#     localVariable = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]',line)
#     if len(localVariable) > 0:
#       mailList.append(localVariable)
# print(mailList)
# we use parentheses with findall to show the especificy
#  party that we would like to take from a string
for line in fhande:
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) >0:
        print(x)