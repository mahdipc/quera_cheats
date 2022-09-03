n, k = input().split()
n, k = int(n), int(k)
c = list(map(int, input().split()))

answer = ((n * k) - sum(c)) // k
print(answer)
