a, b = input().split()
a, b = int(a), int(b)
if a > b:
    a, b = b, a
res = []
for i in range(2, (b-a)+1):
    if (b-a) % i == 0:
        res.append(i)
print(" ".join(map(str, res)))
