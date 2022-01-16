import numpy as np
n = int(input())
st = np.array(list(map(int, input().split())))
print(np.argmax(st)+1)
