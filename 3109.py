import math
n = int(input())

if math.log2(n) == math.floor(math.log2(n)) or math.log2(3*(n+1)) == math.floor(math.log2(3*(n+1))):
    print("Yes")
else:
    print("No")
