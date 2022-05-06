n = int(input())
st = input().split()
for i in range(1, n):
    for j in range(i, 0, -1):
        print(f'{st[i]}: salam {st[j-1]}!')

for i in range(n):
    print(f'{st[i]}: khodafez bacheha!')
    for j in range(i+1, n):
        print(f'{st[j]}: khodafez {st[i]}!')
