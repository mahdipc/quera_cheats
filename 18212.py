digits = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
          '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
s = input()
plus = 0
minus = 0
power = int(s[s.index('e')+1:])
if s.find('.') != -1:
    minus = len(s[s.index('.')+1:s.index('e')])
plus = (power-minus)*digits['0']
for i in s:
    if i == 'e':
        break
    elif i == '.':
        continue
    else:
        plus += digits[i]
print(plus)
