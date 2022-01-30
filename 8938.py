n, m = input().split()
A = [input().split() for i in range(int(n))]
B = [input().split() for i in range(int(m))]
sum = 0
for item in B:
    sum += int(A[int(item[0])-1][int(item[1])-1])
print(sum)
