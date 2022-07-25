n = input().split()
d = {}
result = []
for index in n[1]:
    d[index] = d.get(index, 0) + 1

for i in range(int(n[0])):
    word = input()
    test = {}
    for index in word:
        test[index] = test.get(index, 0) + 1
    if test.keys() == d.keys():
        result.append('Yes')
    else:
        result.append('No')

for row in result:
    print(row)
