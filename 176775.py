n = int(input())

s = 0
for i in range(1, n):
    if n % i == 0:
        s += i

if s > 0 and (s & (s - 1)) == 0:
    print(1)
else:
    print(0)
