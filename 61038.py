import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


n = int(input())
A = [int(input()) for i in range(n)]
res = lcm(A[0], A[1])
for i in A[2:]:
    res = lcm(res, i)
print((res+1) % 30)
