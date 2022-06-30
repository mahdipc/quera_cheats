a, b = input().split()
a, b = int(a), int(b)

if a == 0 and b == 0:
    print('infinite')
elif a == 0:
    print('invalid')
else:
    print('unique')
