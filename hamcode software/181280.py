import numpy as np
n=int(input())
A=[input() for i in range(n)]
intervalA=np.array([list(map(int,i[1:-1])) for i in A])
for i in range(n):
    for j in range(i+1,n):
        intervalA[]