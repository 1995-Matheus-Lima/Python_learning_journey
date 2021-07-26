hours = float(input('enter Hours: '))
rate = float(input('enter rate:'))

if hours <= 40:
    print('Pay: %.2f'%(hours*rate))
else:
    normalValue = 40 * rate
    extravalue = (hours-40)* (rate*1.5)
    print('Pay: %.2f'%(normalValue+extravalue))
    
