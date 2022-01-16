t = int(input())

s = [input().split() for i in range(t)]

for item in s:
    n = int(item[0])
    m = int(item[1])
    tax = int(item[2])
    sum = (m+(n-1)*tax)/(n)-tax
    if (int(sum) != sum) or (sum <= 0):
        print(-1)
    else:
        print(int(sum))
