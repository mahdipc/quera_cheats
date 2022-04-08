import numpy as np
n, c = input().split()
s = np.array(input().split(), dtype=int)
s.sort()
s = s[::-1]


def res(s, cx):
    backpack = []
    s1 = list(s.copy())
    for item in s:
        if item <= cx:
            s1.remove(item)
            backpack.append(item)
            cx -= item
    return backpack, s1


sum = 0
while len(s) > 0:
    backpack, s = res(s, int(c))
    sum += 1
print(sum)
