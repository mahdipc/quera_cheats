list_n = []
while(True):
    n = int(input())
    if n == 0:
        break
    list_n.append(n)
for item in list_n[::-1]:
    print(item)
