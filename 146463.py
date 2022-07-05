n, k = input().split()
n, k = int(n), int(k)
a = [(k//n) for i in range(n)]
for i in range(k % n):
    a[i] += 1

for i in range(n):
    print(*a)
    end_a = a.pop()
    a.insert(0, end_a)
