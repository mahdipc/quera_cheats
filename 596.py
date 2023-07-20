n = int(input())
fib = [1, 2]
s = 3
for i in range(1, n):
    fib.append(fib[i]+fib[i-1])
    s += fib[i]+fib[i-1]

    if s > n*2:
        fib = fib[::-1]
        break

len_fib = len(fib)
# ss = []
# print(fib)
for i in range(len_fib):
    if n-fib[i] >= 0:
        print(len_fib-i, end=" ")
        # ss.append(fib[i])
        n -= fib[i]
# print()
# print(ss)
# print(sum(ss))
