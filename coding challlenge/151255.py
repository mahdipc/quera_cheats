A, B, m = input().split()
A, B, m = int(A), int(B), int(m)
n = int(input())


def get_dice(n):
    res = [B]
    for i in range(n-1):
        res.append((A*res[-1]+B) % m)
    return res


X = get_dice(n)
dice = [(x % 6)+1 for x in X]
print(*dice, sep='\n')
