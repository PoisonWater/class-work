from math import sin
from math import cos
from math import tan

try:
    funcType = input('Which kind of function do you want to integrate? (sin, cos, tan)')
    while funcType != 'sin' and funcType != 'cos' and funcType != 'tan':
        print('Please input the correct form of function name!')
        funcType = input('Which kind of function do you want to integrate? (sin, cos, tan)')
    nEval = eval(input('Please input an n as the number of sub-intervals into which the interval [a, b] will be divided:'))    
    n = int(nEval)
    while type(nEval) is float or n <= 0:
        nEval = eval(input('Please input a positive integer as your n!\nEnter here: '))
        n = int(nEval)    
    a = float(input('Please input the lower bond:'))
    b = float(input('Please input the upper bond:'))
    sums = 0

    if funcType == 'sin':
        for i in range(1, n+1):
            sums += (b-a)/n * sin(a + (i-0.5)*(b-a)/n)
    elif funcType == 'cos':
        for i in range(1, n+1):
            sums += (b-a)/n * cos(a + (i-0.5)*(b-a)/n)
    elif funcType == 'tan':
        for i in range(1, n+1):
            sums += (b-a)/n * tan(a + (i-0.5)*(b-a)/n)
    print('The approximated integral is',sums)
    
except:
    print('Please input the correct form of inputs.')