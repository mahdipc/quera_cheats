n = int(input())
st = [input().split() for i in range(n)]
values = [[int(i[0]), int(i[1])] for i in st]
values.sort()
start = values[0][0]
end = values[-1][1]
if start != 1 or end != 100:
    print(-1)
elif n == 1:
    print(0)
else:
    res=[]
    for i in range(n-1):
        st1=values[i]
        st2=values[i+1]


        if st2[0]<st1[1]:
            if st1[1]>st2[1]:
                if st1 not in res:
                    res.append(st1)
            else:
                if [st1[0],st2[1]] not in res:
                    res.append([st1[0],st2[1]])
        else:
            if values[i+1] not in res:
                res.append(values[i+1])

    # for item in res:
    #     if item[0]==item[1]:
    #         print(-1)
    #         exit()
    print(len(res)-1)
    