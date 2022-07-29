a = input()
b = input()


def inverse(a, b):
    if a == '':
        return -1
    if int(a[0]) > int(b[0]):
        return 1
    elif a[0] == b[0]:
        return inverse(a[1:], b[1:])
    else:
        return 0


if inverse(a[::-1], b[::-1]) == -1:
    print('{} = {}'.format(a, b))
elif inverse(a[::-1], b[::-1]) == 1:
    print('{} < {}'.format(b, a))
else:
    print('{} < {}'.format(a, b))
