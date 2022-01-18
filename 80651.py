ab = [int(input()) for i in range(6)]
sum = 0
for i in range(0, 6, 2):
    sum += min(ab[i], ab[i+1])
print(sum)
