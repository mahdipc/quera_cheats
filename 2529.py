n=int(input())
v=[]
for i in range(n):
    st=input()
    v.append(len(set(st)))
print(max(v))




