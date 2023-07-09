n, m = input().split()
n, m = int(n), int(m)
new_var = [i for i in range(1, n*m+1)]
for i in range(n):
    print(*new_var[i*m:(i+1)*m][::(-1)**i])
