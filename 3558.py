n, m = input().split()

n, m = int(n), int(m)
days_A = []
days_B = []

for i in range(n):
    fr, to = input().split()
    fr, to = int(fr), int(to)
    days_A.extend(list(range(fr, to+1)))


for i in range(m):
    fr, to = input().split()
    fr, to = int(fr), int(to)
    days_B.extend(list(range(fr, to+1)))
sum = 0
for day in days_A:
    if day in days_B:
        sum += 1
print(sum)
