n = int(input())
k = int(input())
res = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(k):
    res = res[-1]+res[:-1]
    res = ''.join([alpha[(alpha.index(item)+1) % 26] for item in res])
print(res)
