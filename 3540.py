l, w, h = input().split()
l, w, h = int(l), int(w), int(h)
isExist = False

for i in range(l // h + 1):
    if (l - i * h) % w == 0:
        print((l - i * h) // w, i)
        isExist = True
        break

if ~isExist:
    print(-1)
