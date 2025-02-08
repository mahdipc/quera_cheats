import string


def u_c(st):
    first = st[0]
    for ch in st:
        if ch != first:
            return None
    return first


s = input()
t = input()
n = int(input())
if (len(s) > n) or (t in s):
    print(-1)
else:
    tuc = u_c(t)
    l = string.ascii_lowercase

    for c in l:
        if tuc == c:
            continue

        if len(s) <= n:
            can1 = s + c * (n - len(s))
            if t not in can1:
                print(can1)
                break

        elif len(s) <= n:
            can2 = c * (n - len(s)) + s
            if t not in can2:
                print(can2)
                break
    else:
        print(-1)
