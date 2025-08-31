t = int(input())
for _ in range(t):
    s = input()
    val = s.split("1")
    c = 0
    for i in val:
        if i != "":
            c += 1
    print(c)
