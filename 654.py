import math
n = int(input())


for a in range(1, n//2):
    b = int((2*a*n-n**2)/(2*a-2*n))
    c = int(-a+n-(2*a*n-n**2)/(2*a-2*n))
    if(a+b+c == n and a**2+b**2 == c**2):
        print(a, b, c)
        break
else:
    print('Impossible')
