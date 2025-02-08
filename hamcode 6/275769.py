def f(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def u(x, y):
    rx = f(x)
    ry = f(y)
    if rx == ry:
        return False
    p[ry] = rx
    return True


n, m, k = input().split()
n, m, k = int(n), int(m), int(k)

r = (n + 1) // 2
c = (m + 1) // 2
A = r * c
if k > A:
    print("-1")
else:
    g = [list("X" * m) for _ in range(n)]
    mp = {}
    iidx = 0
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            g[i][j] = "O"
            mp[(i, j)] = iidx
            iidx += 1
    p = list(range(A))

    d = A - k
    for i in range(0, n, 2):
        for j in range(1, m - 1, 2):
            if d == 0:
                break
            if (i, j - 1) in mp and (i, j + 1) in mp:
                u1 = mp[(i, j - 1)]
                u2 = mp[(i, j + 1)]
                if f(u1) != f(u2):
                    g[i][j] = "O"
                    u(u1, u2)
                    d -= 1
        if d == 0:
            break
    if d > 0:
        for j in range(0, m, 2):
            for i in range(1, n - 1, 2):
                if d == 0:
                    break
                if (i - 1, j) in mp and (i + 1, j) in mp:
                    u1 = mp[(i - 1, j)]
                    u2 = mp[(i + 1, j)]
                    if f(u1) != f(u2):
                        g[i][j] = "O"
                        u(u1, u2)
                        d -= 1
            if d == 0:
                break
    if d > 0:
        for i in range(1, n - 1, 2):
            for j in range(1, m - 1, 2):
                if d == 0:
                    break
                s = []
                for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni = i + di
                    nj = j + dj
                    if (ni, nj) in mp:
                        s.append(mp[(ni, nj)])
                if len(s) < 2:
                    continue
                rts = set(f(x) for x in s)
                if len(rts) >= 2 and (len(rts) - 1) <= d:
                    g[i][j] = "O"
                    rt = None
                    for x in rts:
                        if rt is None:
                            rt = x
                        else:
                            if u(rt, x):
                                d -= 1
                            if d == 0:
                                break
            if d == 0:
                break
    for i in range(n):
        print("".join(g[i]))
