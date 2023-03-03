
s = input().strip()
n = int(input().strip())

count = 0

for i in range(n):
    t = input().strip()
    j = 0
    for c in t:
        if c == s[j]:
            j += 1
            if j == len(s):
                count += 1
                break

print(count)
