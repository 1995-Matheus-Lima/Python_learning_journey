word = "emilyisaxuxuzinho"
countWord = dict()
# for letter in word:
#     if not letter in countWord:
#         countWord[letter] = 1
#     else:
#         countWord[letter] += 1
# print(countWord)
for letter in word:
    countWord[letter] = countWord.get(letter,0) + 1
print(countWord)
