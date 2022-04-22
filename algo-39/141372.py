
import numpy as np
t = int(input())
N = [input() for i in range(t)]
N = [int(i) for i in N]

n = np.max(N)
f = [1]
for i in range(2, n+1):
    f.append(np.gcd(f[-1], i)+i*i)



def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
 
# Driver Code
for n in range(1, 11):
    print("phi(",n,") = ",
           phi(n), sep = "")
            



for n in N:
    print(f[n-1]-n**2)
