abc = input().split()
arr = [input().split() for i in range(3)]
sum = 0
for i in range(200):
    num = 0
    for j in range(3):
        if int(arr[j][0]) <= i and i < int(arr[j][1]):
            num += 1
        if num == 0:
            continue
        sum += num*int(abc[num-1])
print(sum)
