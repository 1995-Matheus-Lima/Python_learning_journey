values = []
while True:
    x = input('Enter a number:')
    if not x == 'done':
        try:
            values.append(float(x.replace(',','.')))
        except:
            print('invalid input')
    else:
        break
if len(values) == 0:
    print(' there isn\'t any value to check')
else:
    print('maximum: %.2f'%max(values))
    print('minimum: %.2f'%min(values))