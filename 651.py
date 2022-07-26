a = input()
b = int(input())
c = int(input())
ab = int(a, b)


def convert_base(number, base):
    if base < 2:
        return False
    remainders = []
    while number > 0:
        remainders.append(str(number % base))
        number //= base
    remainders.reverse()
    return ''.join(remainders)


s = str(convert_base(ab, c))
if s == s[::-1]:
    print('YES')
else:
    print('NO')
