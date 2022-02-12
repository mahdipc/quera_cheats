n, m = input().split()
st = [input() for i in range(int(n))]
count = 0
for item in st:
    for i in item:
        if i == '*':
            count += 1
print(count)
