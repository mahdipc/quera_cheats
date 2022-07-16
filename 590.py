import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


n, m = input().split()
n, m = int(n), int(m)
print(math.gcd(n, m), lcm(n, m))
