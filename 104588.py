n = input().split()
n = list(map(int, n))
sum = 0
for i in n:
    if i >= 80:
        sum += 1

if(sum >= 3):
    print("Mamma mia!")
elif(1 <= sum and sum < 3):
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
