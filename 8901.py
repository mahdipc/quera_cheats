n, p = input().split()

for i in range(int(n)):
    LMR = input().split()
    if LMR[0] == p:
        p = LMR[1]
    elif LMR[1] == p:
        p = LMR[0]

print(p)
