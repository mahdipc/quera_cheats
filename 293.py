from math import sqrt
f1 = int(input())
f2 = int(input())
if f1 < f2:
    nm = f1
    m = f2
else:
    nm = f2
    m = f1


def isPrime(n):
    prime_flag = 0

    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print(n)


for i in range(int(nm), int(m)+1):
    isPrime(i)
