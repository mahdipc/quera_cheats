def count_ways_to_step(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 else 0) + \
            (dp[i - 5] if i >= 5 else 0)

    return dp[n]


n = int(input())

print(count_ways_to_step(n))
