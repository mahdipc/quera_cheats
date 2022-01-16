t = int(input())

for i in range(t):
    number = input()
    flag = 0
    d = len(number)
    startP = d*9
    n = int(number)
    if n-startP < 0:
        startP = 0
    else:
        startP = -startP+n
    for i in range(startP, n):
        sum_of = i+sum(int(digit) for digit in str(i))
        if sum_of == n:
            flag = 1
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")
