def devide(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result


a, b, x = input().split()
a,b,x = int(a), int(b), int(x)
a_list = devide(a)
b_list = devide(b)
counter = 0
for i in a_list:
    for j in b_list:
        if i+j <= x:
            counter += 1
print(counter)
