n = int(input())
a = input().split()
b = input().split()
res = 0
for i in range(n):
    res += int(a[i])*int(b[i])
print(res)
