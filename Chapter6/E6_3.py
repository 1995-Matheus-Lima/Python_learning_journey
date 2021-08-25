def countingLetter(wordEnter,letterEnter):
    word = wordEnter
    count = 0
    for letter in word:
        if letter == letterEnter:
            count = count + 1
    print(count)

countingLetter('emanuele', 'e')