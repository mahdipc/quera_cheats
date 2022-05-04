import random

n, b, m = input().split()
n = int(n)
b = int(b)
m = int(m)


def hash(st, b, m):
    ret = 0
    for i in range(len(st)):
        ret = (ret * b + (ord(st[i]) - ord('a'))) % m
    return ret


alpha = list('abcdefghijklmnopqrstuvwxyz')
while True:
    random.shuffle(alpha)
    s = ''.join([alpha[random.randint(0, len(alpha)-1)] for i in range(n)])
    t = ''.join([alpha[random.randint(0, len(alpha)-1)] for i in range(n)])

    if hash(s, b, m) == hash(t, b, m):
        break
print(s)
print(t)
