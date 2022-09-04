import math
m = int(input())
n = 0
list_z = []
for i in range(1, 2500):
    list_z.append(i+n)
    n = (n+i)


def maghsom(n):
    t = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            t.extend([i, n//i])
    t.extend([n])
    return list(set(t))


for i in list_z:
    if len(maghsom(i)) >= m:
        print(i)
        break
