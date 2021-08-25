import re
fhande = open("mbox-short.txt", "r")

for line in fhande:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)