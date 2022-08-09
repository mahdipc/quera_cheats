n = int(input())
b = (n//2+1)//2
res = b*(b+1) - (n//2)*b + (n//3)-b
k = (n//3)//2
res += (n+1)*k-3*k*(k+1)

if n//3 % 2 == 1:
    res += (n - 3*(2*k+1)) // 2
print(res)
