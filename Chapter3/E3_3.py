score = input('Enter Score: ')

try:
    score = float(score)
    if score >= 0 and score < 0.6:
        print('F')
    elif score >= 0.6 and score < 0.7:
        print('D')
    elif score >= 0.7 and score < 0.8:
        print('C')
    elif score >= 0.8 and score < 0.9:
        print('B')
    elif score >= 0.9 and score <= 1:
        print('A')
    else:
        print('Bad Score')
except:
        print('Bad Score')