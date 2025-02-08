n, q = map(int, input().split())
s = bytearray(input().strip(), "ascii")

for _ in range(q):
    query = input().split()

    if query[0] == "?":
        print("YES" if query[1].encode() in s else "NO")
    else:
        k = int(query[1]) - 1
        s[k] ^= 1
