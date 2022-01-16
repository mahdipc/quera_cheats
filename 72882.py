import numpy as np

n, m = input().split()
st = [input().count('*') for j in range(2*int(n))]
s = np.array(st)
print(str(np.sum(s[:int(n)]))+' '+str(np.sum(s[int(n):])))
