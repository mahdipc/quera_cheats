a, b, c = input().split("?")
a, b, c = int(a), int(b), int(c)

t1 = a * (b + c)
t2 = (a + b) * c

t4 = a * b * c
t5 = a + b + c
print(max(t1, t2, t4, t5))
