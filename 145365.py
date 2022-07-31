import numpy as np
n, m = input().split()
n, m = int(n), int(m)
matrix = np.zeros((n, n), dtype=int)
for i in range(m):
    x, y = input().split()
    x, y = int(x)-1, int(y)-1
    matrix[x, y] = matrix[y, x] = 1
for i in range(n):
    print(*matrix[i], sep='')
