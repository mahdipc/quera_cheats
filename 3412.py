l = []
for i in range(4):
    person = list(input().split())
    if person[1] != 'U':
        if person[1] == 'L':
            l.insert(0, person[0])
        else:
            l.append(person[0])

print(l[1])
