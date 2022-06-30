import numpy as np
k = int(input())
n = 1
while True:
    s = np.sin(n)
    if 0 <= s and s <= 1/k:
        print(n)
        break
    n += 1
