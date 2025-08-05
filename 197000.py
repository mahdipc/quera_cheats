n = int(input())
target = 1
for i in range(n):
    a, b = map(int, input().split())
    if a == target:
        target = b
print(target)
