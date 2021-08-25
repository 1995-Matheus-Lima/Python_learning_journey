#when python is evaluating a expression as (x > 2) and ( x/4 > 2); 
#python start from left to rigth and on the first false it stop the
#avaluation and returns false. it's called short circuit
x = 1
y = 0
if x > 2 and x/y > 3:
    print('works')
else:
    print('first example works well')
x = 8
if x > 2 and x/y > 3:
    print('works')
else:
    print('first example works well')

#  He can see that in the first example works well and still with
#  the division by zero but why it don't show us the error?
#  because the short circuit make it exit and check that x > 2 is false. 

# Short circuit: When Python is part-way through evaluating a logical expression
# and stops the evaluation because Python knows the final value for the ex-
# pression without needing to evaluate the rest of the expression.