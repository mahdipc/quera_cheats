s, f, l, x = input().split()
s, f, l, x = int(s), int(f), int(l), int(x)
if x < s:
    print('exam did not started!')
elif x >= f:
    print('exam finished!')
else:
    print(min(f-x, l))
