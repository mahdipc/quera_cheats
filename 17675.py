n = int(input())


def fib(n):
    fib = [1, 2]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib


f = fib(10)
for i in range(1, n+1):
    if i in f:
        print("+", end='')
    else:
        print("-", end='')
