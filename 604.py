n=input()
n=int(n)
if n==2:
    print("1")
else :
    
    arr=[0]*n
    kiled=0
    j=1
    is_remove=1
    while 1:
        if arr[j]==0:
            if is_remove==1:
                arr[j]=1
                kiled+=1
                is_remove=0
            else : 
                is_remove=1
        j+=1
        j%=n
        if kiled==n-1:
            break


    for i in range(0,n):
        if arr[i]==0:
            print(i+1)
            break
    