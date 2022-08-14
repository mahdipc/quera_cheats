import math
x = int(input())
n = int(input())
ex = 0
for i in range(n):
    ex += x**i/math.factorial(i)
print(f'{ex:.3f}')
