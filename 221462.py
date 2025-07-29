x = {}
y = {}
z = {}
for i in range(7):
    x1, y1, z1 = input().split()
    x1, y1, z1 = int(x1), int(y1), int(z1)
    x[x1] = x[x1] + 1 if x1 in x else 1
    y[y1] = y[y1] + 1 if y1 in y else 1
    z[z1] = z[z1] + 1 if z1 in z else 1

for i in x:
    if x[i] == 3:
        print(i, end=" ")
for i in y:
    if y[i] == 3:
        print(i, end=" ")
for i in z:
    if z[i] == 3:
        print(i, end=" ")
