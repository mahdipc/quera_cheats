n = int(input())
pieces = list(map(int, input().split()))
print(sum(pieces) + 3 * (n - 1))
