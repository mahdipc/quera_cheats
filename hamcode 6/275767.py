n = int(input())
sum = 0
for i in range(1, n):
    sum += i
    print(i, end=" + ")

print(n, "=", sum + n)
