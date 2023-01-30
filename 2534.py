n = int(input())
st = [int(input()) for i in range(n)]
avg = int(sum(st)/n)

min = 0
for item in st:
    if item >= avg:
        continue
    min += avg - item

print(min)
