import math
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))), end=" ")
    print()
