X=int(input())
N=int(input())
a=0
if N==0:
    a=20
elif N==7:
    a=X
else:
    a=X-N
if a>0:
    print(a)
else:
    print(0)