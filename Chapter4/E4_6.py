def computation(hours,rate):
    if hours <= 40:
        print('pay: %.2f'%(hours*rate))
    else:
        normal = 40 * rate
        extra = (hours-40)*rate*1.5
        print('pay: %.2f'%(normal + extra))

computation(40,10)