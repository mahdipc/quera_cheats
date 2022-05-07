def calculator(n, m, li):
    sm=0
    j=0
    for i in range(0,n,m):
        sm+=(-1)**j*sum(li[i:i+m])
        j+=1

    return sm