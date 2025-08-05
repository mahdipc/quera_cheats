t1 = input().split()
t2 = input().split()
t1 = list(map(int, t1))
t2 = list(map(int, t2))
cnt = 0
for i, j in zip(t1, t2):
    if i == 0:
        continue
    if i == j:
        cnt += 1
print(cnt)
