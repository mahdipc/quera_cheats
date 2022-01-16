n=int(input())
listitem=[[j for j in input().replace(" ", "").split()] for i in range(2*n)]
count=0
for i in range(0,2*n,2):
    if len(listitem[i][0])!=len(listitem[i+1][0]):
        count+=1
print(count)