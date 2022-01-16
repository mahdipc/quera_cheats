import numpy as np
n = int(input())
a = np.array(range(1, n+1))
aa = np.outer(a, a)
for aas in aa:
    print(' '.join(map(str, aas)))
