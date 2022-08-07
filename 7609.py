s = input()
result = 'khoob'
d = {}
for index in s:
    d[index] = d.get(index, 0) + 1

for val in d.values():
    if val % 2 == 1:
        result = 'bad'
        break

print(result)
