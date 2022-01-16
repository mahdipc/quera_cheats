
n,k= [int(j) for j in input().split()]
c=[int(j) for j in input().split()]

if k==1:
    print(max(c))
elif k==2:
    print(min([c[0],c[n-1]]))
else:
    print(min(c))
