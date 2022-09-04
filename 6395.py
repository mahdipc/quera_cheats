import numpy as np
n = int(input())
a = input().split()
a = np.array(a, dtype=np.int)
sum = 0
sub = 0
for i in range(n):
    sum -= a[i]
    if sum < 0:
        sub += abs(sum)
        sum = 0
print(sub)
