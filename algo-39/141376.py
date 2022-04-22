from distutils.log import debug
import numpy as np
t = int(input())
N = [int(input()) for i in range(t)]
for n in N:
    A = list(range(2, n+2))
    gcd = np.lcm.reduce(A)
    for a in A:
        print(a, end=' ')
    kk = n+1
    tt = 1
    while kk > 1:
        gg = gcd*tt
        if gg not in A:
            print(gg, end=' ')
            kk -= 1
        tt += 1

    print()
