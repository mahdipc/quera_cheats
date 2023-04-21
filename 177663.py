nn, a, b, c, d = input().split()
nn, a, b, c, d = int(nn), int(a), int(b), int(c), int(d)
sum = 0
for n in range(1, nn+1):
    if (n % a == 0 and n >= a) or (n % b == 0 and n >= b) or (n % c == 0 and n >= c) or (n % d == 0 and n >= d):
        sum += 1
print(sum)
