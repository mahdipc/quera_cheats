
n = int(input())
m = 0
while n > 4:
    n -= 4
    m += 1

if n % 4 == 0:
    print(-m - 1, m + 1)

elif n == 1:
    print(-m, -m)

elif n == 2:
    print(m + 1, -m)

elif n == 3:
    print(m + 1, m + 1)
