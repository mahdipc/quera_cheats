n, m = input().split()
n, m = int(n), int(m)
error = []
sum_bi = 0
for i in range(n):
    ai, bi = input().split()
    ai, bi = int(ai), int(bi)
    error.append((ai - bi))
    sum_bi += bi
error.sort(reverse=True)
print(sum_bi + sum(error[:m]))
