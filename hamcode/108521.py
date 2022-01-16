import numpy as np
n, a, b = map(int, input().split())
A = np.array(list(map(int, input().split())))
ind_vasat = 0
for i in range(len(A)-1):
    if(A[i] > A[i+1]):
        ind_vasat = i
        break
secend = A[ind_vasat+1:]
first = A[:ind_vasat+1]

if all(first <= 45+a) & all(first == np.sort(first)) & all(secend <= 90+b) & all(secend == np.sort(secend)):
    print("YES")
else:
    print("NO")
