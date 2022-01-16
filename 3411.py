import math
n = int(input())
s = str(math.factorial(n))

for i in range(len(s), 0, -1):
    if s[i-1] != '0':
        print(s[i-1])
        break
