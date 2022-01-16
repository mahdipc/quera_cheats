n,k= [int(j) for j in input().split()]
i=1
conut=0
while True:
    i=(i+k)%n
    conut+=1
    if i==1:
        print(conut)
        break

