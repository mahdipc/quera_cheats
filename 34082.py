n, k = input().split()
n, k = int(n), int(k)
arr = input().split()
arr = list(map(int, arr))

sum = 0
counter = 1
i = 0
while i <n:
    sum += arr[i]
    i += 1
    if sum > k:
        sum = 0
        counter += 1
        i -= 1
print(counter)
