n, x, k = input().split()
n, x, k = int(n), int(x), int(k)
st = [input() for i in range(n)]

if x+k > n:
    print(st[(x+k) % n-1])
else:
    print(st[x+k-1])
