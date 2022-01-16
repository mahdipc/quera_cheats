x1,x2=input().split(' ')
x1,x2=int(x1),int(x2)
if x1==x2:
    print('Saal Noo Mobarak!')
elif x1<x2:
    print('R'*(x2-x1))
else:
    print('L'*(x1-x2))
