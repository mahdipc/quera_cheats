import numpy as np
n = int(input())
A = np.array([int(input()) for i in range(n)])
first_inteerval = 100
end_interval = 0
for i in range(n):
    end_interval += np.sum(A[i]*A[i+1:])
end_interval = 2*end_interval


arr_sharifi = [153, 370, 371, 407, 1634, 8208,
               9474, 54748, 92727, 93084, 548834, 1741725]


def is_sharifi(number):
    number_list = list(map(int, str(number)))
    len_ = len(number_list)
    return number == sum([i**len_ for i in number_list])


for num in arr_sharifi:
    if num <= end_interval:
        print(num)
    else:
        break
