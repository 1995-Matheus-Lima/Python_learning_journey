import string
def frequency(file):
    try:
        fhande = open((file),'r')
        alphabet = dict()
        totalLetters = 0
        for line in fhande:
            for character in line:
                if character in string.punctuation + '0123456789\n' or character == ' ':continue
                char = character.lower()
                alphabet[char] = alphabet.get(char,0) + 1
                totalLetters += 1
        alphabetList = list()
        for letter, value in alphabet.items():
            alphabetList.append((letter,value))
        alphabetList.sort()
        for letter in alphabetList:
            print('%s : %.2f'%(letter[0],letter[1]/totalLetters))
    except:
        print('file don\'t finded: %s'%file)

frequency(input('Enter a file name: '))