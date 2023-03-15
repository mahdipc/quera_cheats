n = int(input())

count = 1
while True:
    if int(bin(count)[2:]) <= n:
        count += 1
    else:
        break
print(count-1)
