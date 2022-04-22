n, q = input().split()
n = int(n)
q = int(q)
S = input().split()
S = [int(i) for i in S]
K = [input() for i in range(q)]


def fast_exp(n, pow, mod):
    if n == 0 or n == 1:
        return n % mod
    if pow == 0:
        return 1
    if mod == 1:
        return 0
    ans = 1
    while pow > 0:
        if pow % 2 == 1:
            ans = (ans*n) % mod
        n = (n*n) % mod
        pow = pow//2
    return ans


def fibonacci(S, n):
    sum = 0
    for i in S:
        sum += i
    ln = n-len(S)-1
    return sum*fast_exp(2, ln, (10**9+7)) % (10**9+7)


for k in K:
    print(fibonacci(S, int(k)))
