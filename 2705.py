p, d = input().split()
p, d = int(p), int(d)
hp = p//2
i = 1
while (d*i) % p > hp:
    i += 1
print(d*i)
