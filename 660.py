n = int(input())
budget = {}
gift = {}
for i in range(n):
    k = input()
    budget[k] = 0
    gift[k] = 0
for i in range(n):
    k = input()
    m, l = map(int, input().split(' '))
    if l != 0:
        if m % l != 0:
            a = m - m % l
            budget[k] -= a
            a = int(a/l)
            for i in range(l):
                name = input()
                gift[name] += a
        else:
            budget[k] -= m
            for i in range(l):
                name = input()
                a = int(m/l)
                gift[name] += a

for i in budget.keys():
    print(i, budget[i]+gift[i])
