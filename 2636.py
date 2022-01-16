import numpy as np
st = input().split()
n = np.array(st, dtype=np.int)
z = np.array([1, 1, 2, 2, 2, 8])
print(" ".join(map(str, z-n)))
