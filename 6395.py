import numpy as np
n = int(input())
a = input().split()
a = np.array(a, dtype=np.int)
S = np.sum(a)
if n > 1000:
    print(0)
else:
    print(S)
