n = int(input())
st1 = input()
st2 = input()
sum = 0
for i in range(len(st1)):
    if st1[i] != st2[i]:
        sum += 1
print(sum)
