import numpy as np
n = int(input())
A = list(map(int, input().split()))
cite = sorted(A, reverse=True)
res = sum(x >= i + 1 for i, x in enumerate(cite))
print(res)
