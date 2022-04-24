n = int(input())
st = [input() for i in range(n)]
st = [i.lower() for i in st]
for element in st:
    res = element.split()
    for i in res:
        print(i[0].upper()+i[1:], end=" ")
    print()
