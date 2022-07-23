from math import ceil


T = int(input())
lines = [input() for i in range(T)]
for line in lines:
    n, m, a, b = line.split()
    n, m, a, b = int(n), int(m), int(a), int(b)

    l = (n-a+1)/(2*a-1)
    r = (m-b+1)/(2*b-1)

    print(ceil(l)*ceil(r))
