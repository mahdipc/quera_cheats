import numpy as np
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for i in range(k)]
mtx = np.zeros((n, m, k))
st = np.concatenate(([np.power(2, i) for i in range(30)],
                     [np.power(2, 30+i, dtype=float) for i in range(20)]))
index_k = 0
for item_x in A:
    li = item_x[2]
    ri = item_x[0]-1
    ci = item_x[1]-1
    mtx[ri:ri+li, ci:ci+li, index_k] = st[index_k]
    index_k += 1

ss = np.sum(mtx, axis=2)
print(np.sum(np.unique(ss) != 0))
