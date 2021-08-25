import re

fhand = open('mbox-short.txt', 'r')
# dot, when you use dot we search for any character. F..M , will match if it is FROM, FxxM ,F12m, F@#M
for line in fhand:
    line = line.rstrip()
#     if re.search('F..m:',line):
#         print(line)

# plus sign, we use plus after dot('.+') when we want to seach search more than one character after or before a character
    if re.search('From:.+@',line):
        print(line)

