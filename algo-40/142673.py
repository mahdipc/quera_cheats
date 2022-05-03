def make_change(goal, coins):
    wallets = [[coin] for coin in coins]
    new_wallets = []
    collected = []

    while wallets:
        for wallet in wallets:
            s = sum(wallet)
            for coin in coins:
                if coin >= wallet[-1]:
                    if s + coin < goal:
                        new_wallets.append(wallet + [coin])
                    elif s + coin == goal:
                        collected.append(wallet + [coin])
        if len(new_wallets) > m:
            break
        wallets = new_wallets
        new_wallets = []
    return collected


n, m = map(int, input().split())
# n, m = 5, 3
coins = []
for i in range(1, n+1):
    if n % i != 0:
        coins.append(i)
if len(coins) < m:
    print(-1)
else:
    changes = make_change(n, coins)
    isbreak = False
    for item in changes[::-1]:
        setItem = list(set(item))

        if len(setItem) <= m:
            resu = m-len(setItem)
            for coin in coins:
                if coin not in setItem and resu != 0:
                    setItem.append(coin)
                    resu -= 1
            if len(setItem) == m:
                print(*setItem)
                isbreak = True
                break
    if not isbreak:
        print(-1)
