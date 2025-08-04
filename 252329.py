import math

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            b = n // a

            if a < b:
                if (b - a) % 2 == 0:
                    count += 1
    print(count)
