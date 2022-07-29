a, b, n = input().split()
a, b, n = int(a), int(b), int(n)

if n % 2 == 0:
    answer = n/2 * (a+b)
else:
    answer = (n-1)/2 * (a+b) + a

print(int(answer))
