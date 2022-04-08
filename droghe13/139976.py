n = int(input())


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


if (n % 2 != 0) and isPrime(n):
    print("zoj")
else:
    print("fard")
