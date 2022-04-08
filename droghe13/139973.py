def isTringle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False


st = input().split()
b = False

for i in range(5):
    for j in range(5):
        for k in range(5):
            if i != j and i != k and j != k:
                if isTringle(int(st[i]), int(st[j]), int(st[k])):
                    b = True
                    break


if b:
    print("YES")
else:
    print("NO")
