
def checkUntil(num, K, N, ans):
    if (N == 1):
        ans.append(num)
        return

    if ((num % 10 + K) <= 9):
        checkUntil(10 * num +
                   (num % 10 + K),
                   K, N - 1, ans)

    if (K):
        if ((num % 10 - K) >= 0):
            checkUntil(10 * num +
                       num % 10 - K,
                       K, N - 1, ans)


def check(K, N, ans):
    for i in range(1, 10):
        checkUntil(i, K, N, ans)


N, K = [int(j) for j in input().split()]

ans = []
check(K, N, ans)
ans.sort()
print(",".join(map(str, ans)))
