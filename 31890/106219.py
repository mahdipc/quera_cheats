import numpy as np
from math import sqrt


def isprime(num):
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


n, m, k = [int(j) for j in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(n)]
matrix = np.array(matrix)
i = 0
j = 0
for kk in range(k):
    aij = matrix[i, j]
    if isprime(aij) == False:
        res = aij % 4
        if res == 0:
            j = (j+1) % m
        elif res == 1:
            i = (i+1) % n
        elif res == 2:
            j = (j-1) % m
        else:
            i = (i-1) % n
    else:
        i, j = n-i-1, m-j-1
print(i+1, end=' ')
print(j+1)
