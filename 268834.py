n = int(input())

count = 0

for _ in range(n):
    s = input().strip().lower()
    if s == 'rayancode':
        count += 1

print(count)
