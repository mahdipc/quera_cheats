import numpy as np

a = [[int(j) for j in input().split()] for i in range(3)]
a = np.array(a)
X = a[:, 0]
Y = a[:, 1]
# print(Y)
x = 0
y = 0
for target_list in a:
    if np.count_nonzero(X == target_list[0]) == 1:
        x = target_list[0]
    if np.count_nonzero(Y == target_list[1]) == 1:
        y = target_list[1]
print(x, y)
