T = input()
n = int(input())
ss = [input() for i in range(n)]


def isSub(S, T):
    S_d = S
    for item in S:
        if item not in T:
            S_d = S_d.replace(item, '', 1)
    if S_d == T:
        return True
    return False


sum = 0
for s in ss:
    if T in s:
        sum += 1
    elif isSub(s, T):
        sum += 1

print(sum)
