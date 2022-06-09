n = int(input())

ss = []
sn = "1"
for i in range(2, n+1):
    sn = sn+str(i)+sn

    ss.append(sum(map(int, list(sn))))
print(ss)
