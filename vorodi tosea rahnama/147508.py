import math
T = int(input())
lines = [int(input()) for i in range(T)]
for n in lines:
    squere = n**2
    count = 0
    value_dic = {}
    for i in range(1, n):
        b = math.sqrt(squere-i*i)
        if b == int(b) and min(i, b) not in value_dic:
            count += 1
            value_dic[min(i, b)] = 1
    print(count)
