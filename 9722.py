n = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


list_prime = ["2", "3", "5", "7"]

if n == 1:
    print(*list_prime, sep='\n')
else:
    for i in range(2, n+1):
        for i in range(10):
            for p in list_prime:
                if p+str(i) not in list_prime and len(p) < n and is_prime(int(p+str(i))):
                    list_prime.append(p+str(i))
list_prime.sort()
for p in list_prime:
    if len(p) == n:
        print(p)
