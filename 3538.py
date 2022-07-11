n=int(input())
st1=input()
n=int(input())
st2=input()
n=int(input())
st3=input()

st=(st1+" "+st2+" "+st3).split()
days=["shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"]
count=0
for day in days:
    if day not in st:
        count +=1
print(count)
