T = int(input())
lines = [input() for i in range(T)]
for line in lines:
    n, m, a, b = line.split()
    n, m, a, b = int(n), int(m), int(a), int(b)

    l = a+(a-1)
    r = b+(b-1)

    print((round(n/r*m/l), round(m/r*n/l)))
