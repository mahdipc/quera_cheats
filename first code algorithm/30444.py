import numpy as np

q = int(input())
sts = [input() for j in range(q)]

for st in sts:
    a, b = st.split()
    a, b = int(a), int(b)
    res = np.ceil(np.sqrt(b))-np.ceil(np.sqrt(a))+1

    if (np.ceil(np.sqrt(b)) != np.sqrt(b)):
        res = res-1
    print(int(res))
