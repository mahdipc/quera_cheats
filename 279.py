from math import factorial


a, x, n = input().split()
a, x, n = int(a), int(x), int(n)
s = 0
for k in range(n+1):
    s += x**k*a**(n-k) * factorial(n)/factorial(k)/factorial(n-k)
print(int(s))
