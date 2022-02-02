n, m = input().split()
n = int(n)
m = int(m)
div = n//m
if n % m == 0:
    print(div)
else:
    print(div+1)
