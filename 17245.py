A1 = input()
A2 = input()
A3 = input()
for i in range(0, len(A1), 5):
    if A1[i:i+5] == '*'*5:
        print('T', end='')
    elif A1[i:i+5] == 'oo*oo' and A2[i:i+5] == 'o***o' and A3[i:i+5] == '*ooo*':
        print('A', end='')
    elif A1[i:i+5] == '*ooo*' and A2[i:i+5] == 'oo*oo' and A3[i:i+5] == '*ooo*':
        print('X', end='')
    elif A1[i:i+5] == '**o**' and A2[i:i+5] == '*o*o*' and A3[i:i+5] == '*ooo*':
        print('M', end='')
    elif A1[i:i+5] == '*ooo*' and A2[i:i+5] == '*o*o*' and A3[i:i+5] == '*ooo*':
        print('N', end='')
