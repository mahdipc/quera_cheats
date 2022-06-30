import numpy as np
k = int(input())
if k == 1:
    print(1)
else:
    for c1 in range(100):
        if 2*np.pi*c1 < np.arcsin(1/k)+2*np.pi*c1:
            print(int(np.arcsin(1/k)+2*np.pi*c1))
            break
        elif np.pi-np.arcsin(1/k)+2*np.pi*c1 < np.pi+2*np.pi*c1:
            print(int(np.pi+2*np.pi*c1))
            break
