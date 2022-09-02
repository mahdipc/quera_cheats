n = input()
if len(n) == 1:
    if n[0] == '1':
        print(1)
        exit()
    elif n[0] == '2':
        print(2)
        exit()
n = [int(i) for i in n]
for ind, val in enumerate(n[::-1]):
    if val != 0:
        n[len(n)-ind-1] = val-1
        break
    n[len(n)-ind-1] = 9
    n[len(n)-ind-2] = (n[len(n)-ind-2])-1
if n[0] == 0:
    n.pop(0)
print(*n, sep="")
