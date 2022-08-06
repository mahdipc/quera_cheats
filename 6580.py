x, y = input().split()
x, y = int(x), int(y)
r = int(input())
dx, dy = input().split()
dx, dy = int(dx), int(dy)

if dx >= x and dx <= x+r and dy <= y and dy >= y-r:
    print('Mahdi')
else:
    print('Parsa')
