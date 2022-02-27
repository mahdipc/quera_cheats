n = int(input())
s = [input() for i in range(n)]
isCapsLock = False
res = []
for item in s:
    if item == "CAPS":
        isCapsLock = ~isCapsLock
    else:
        if isCapsLock:
            res.append(item.upper())
        else:
            res.append(item)
print("".join(res))
