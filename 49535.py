n, k = [int(j) for j in input().split()]
c = [int(input()) for j in range(n)]
if sum(c) >= k:
    print("YES")
else:
    print("NO")
