n = int(input())
lists = [int(j) for j in input().split()]
k = int(input())


chance = 0

for ss in range(k, 0, -1):
    choose = max(lists)
    i = lists.index(choose)
    lists[i] = lists[i]-1
    chance = chance+choose

print(chance)
