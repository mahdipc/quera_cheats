def conv(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def poly_pow(p, n):
    res = [1]
    base = p[:]
    while n > 0:
        if n & 1:
            res = conv(res, base)
        base = conv(base, base)
        n >>= 1
    return res


m, n = map(int, input().split())
coeffs = list(map(int, input().split()))

ans = poly_pow(coeffs, n)
print(" ".join(map(str, ans)))
