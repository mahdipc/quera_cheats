n = int(input())
st = input()
first = st[: n ]
secend = st[n  :]
for i in range(len(first)):
    if first[i] == secend[i]:
        print("NO")
        break
else:
    print("YES")
