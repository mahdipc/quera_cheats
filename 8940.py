n, p, q = input().split()
n, p, q = int(n), int(p), int(q)
st = [input() for i in range(n)]
res = []
for item in st:
    res.append(item[:p]+item[-q:])
print(len(set(res)))
