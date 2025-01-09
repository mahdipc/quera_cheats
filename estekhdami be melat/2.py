n, m = input().split()
n, m = int(n), int(m)
khales = [0] * (n + 1)

for i in range(m):
    u, v, w = input().split()
    u, v, w = int(u), int(v), int(w)
    khales[u] -= w
    khales[v] += w


if sum(khales) != 0:
    print(0)

d = []
c = []

for i in range(1, n + 1):
    if khales[i] < 0:
        d.append((i, -khales[i]))
    elif khales[i] > 0:
        c.append((i, khales[i]))

result = []
i, j = 0, 0

while i < len(d) and j < len(c):
    bedehkar, bestankar = d[i]
    mabda, magsad = c[j]

    amount = min(bestankar, magsad)
    result.append((bedehkar, mabda, amount))

    d[i] = (bedehkar, bestankar - amount)
    c[j] = (mabda, magsad - amount)

    if bestankar - amount == 0:
        i += 1
    if magsad - amount == 0:
        j += 1

print(len(result))


for u, v, w in result:
    print(u, v, w)
