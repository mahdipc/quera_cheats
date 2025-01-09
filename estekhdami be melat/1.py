n = int(input())


fib = [1, 2]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])

count = 0
i = len(fib) - 1

while n > 0 and i >= 0:
    while fib[i] <= n:
        n -= fib[i]
        count += 1
    i -= 1

print(count)
