
n = int(input())
if n <= 2:
    print(n)
else:
    temp = [1, 2]
    for x in range(n - 2):
        temp.append((temp[-1] + temp[-2]))
    print(temp[-1])
