n = int(input())
a = input().split()
a = [int(i) for i in a]
q = int(input())
for i in range(q):
    s, k = input().split()
    s, k = int(s), int(k)
    sum = 0
    for j in range(s, n+1, k):
        sum += a[j-1]
    print(sum)
