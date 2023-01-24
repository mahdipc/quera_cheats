import numpy as np
n = int(input())
s = input().split()
s = np.array([int(i) for i in s])
sum = np.sum(s//np.gcd.reduce(s))

print(sum)
