import numpy as np
n, m, k = input().split()
n, m, k = int(n), int(m), int(k)
A = np.zeros((n, m))
for i in range(k):
    r, c = input().split()
    A[int(r)-1, int(c)-1] = 1
if k == 0:
    print(1)
    print(1, 1)
elif k % 2 == 1:
    print(0)
elif k == n*m:
    print(-1)
else:
    for i in range(n):
        for j in range(m):
            if A[i, j] == 0:
                print(1)
                print(i+1, j+1)
                exit()
