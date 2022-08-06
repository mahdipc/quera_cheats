n, k = input().split()
n, k = int(n), int(k)
fruit = [input().split() for i in range(n)]


fruit.sort(key=lambda x: int(x[0]))
for i in range(n):
    if int(fruit[i][0]) <= k and int(fruit[i][0]) < int(fruit[i][1]):
        k += int(fruit[i][1])-int(fruit[i][0])

print(k)
