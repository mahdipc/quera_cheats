n, q = input().split()
n, q = int(n), int(q)
s = input()

for i in range(q):
    st = input().split()
    if st[0] == "?":
        t = st[1]
        print("YES" if t in s else "NO")
    else:
        k = int(st[1]) - 1
        s = s[:k] + ("1" if s[k] == "0" else "0") + s[k + 1 :]
