
a = input()
if int(a[-1]) not in [1, 3, 7, 9]:
    print(-1)
else:
    a = int(a)
    i = 0
    res = 0
    while True:
        res = (res * 10 + 1) % a
        if res == 0:
            sum_value = int('1'*(i+1))
            print(sum_value//a)
            break
        if i > 100000:
            print(-1)
            break
        i += 1
