t = int(input())
rows = [input().split() for i in range(t)]
for row in rows:
    a, b, c, d = row
    a, b, c, d = int(a), int(b), int(c), int(d)
    if a+c > b+d:
        print("perspolis")
    elif a+c < b+d:
        print("esteghlal")
    elif a < d:
        print("perspolis")
    elif b > c:
        print("esteghlal")
    else:
        print("penalty")
