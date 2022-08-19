
m, s = input().split()
m, s = int(m), int(s)

res = []
r = s % 9
d = s//9
if s == 0 or m*9 < s:
    print(-1, -1)
else:
    s_min = [1]+[0]*(m-d-2)+[r-1] + [9]*d
    if s < 10:
        s_min = [1]+[0]*(m-2)+[s-1]
    if m == 2:
        for i in range(10, 100):
            if sum([int(j) for j in str(i)]) == s:
                s_min = [int(j) for j in str(i)]
                break
    s_max = d*[9]+[r]+(m-d-1)*[0]

    print(*s_min, sep='', end=' ')
    print(*s_max, sep='')
