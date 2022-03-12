import numpy as np
import math
n = int(input())


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


count = 0
sum = 0
for i in range(1, n+1):
    item = list(divisorGenerator(i))
    sum += np.sum(item)
    count += len(item)


print(int(count), int(sum))
