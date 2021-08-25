hours =input('enter Hours: ')
rate = input('enter rate:')

try:
    hours = float(hours)
    rate = float(rate)
    if hours <= 40:
        print('Pay: %.2f'%(hours*rate))
    else:
        normalValue = 40 * rate
        extravalue = (hours-40)* (rate*1.5)
        print('Pay: %.2f'%(normalValue+extravalue))
except:
    print('Error, please enter a numeric input')