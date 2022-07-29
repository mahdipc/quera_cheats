t = int(input())
x = []
y = []
for i in range(t):
    a, b = input().split()
    x.append(int(a))
    y.append(int(b))


res = []

for j in range(t):
    c1 = 0
    c2 = 2
    for i in range(y[j]):
        if i % 2 == 0:
            c1 += 1
            c2 += 1
        else:
            c1 += 3
            c2 += 3
    if x[j] == y[j]:
        print(c1)
    elif abs(x[j]-y[j]) == 2:
        print(c2)
    else:
        print(-1)
