from math import sqrt
n = input()
s = 0
for i in n:
    s += int(i)


def isprime(num):
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


n = int(n)
while True:
    n += 1
    if isprime(n):
        s -= 1
    if s == 0:
        print(n)
        break
