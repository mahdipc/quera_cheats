n = int(input())
if n % 2 == 0:
    print(n//2)
else:
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res = i
    print(res)
