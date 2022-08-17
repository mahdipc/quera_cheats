import numpy as np
n = int(input())
mat = [input().split() for i in range(n)]
mat = [list(map(float, i)) for i in mat]
det = np.linalg.det(mat)
print(f'{det:.2f}')
