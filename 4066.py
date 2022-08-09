n, m = input().split()
n, m = int(n), int(m)


d = {}
for i in range(n):
    words = input().split()
    d[words[0]] = words[1]

words = input().split()
for word in words:
    exist = d.get(word, '')
    if word in d:  # exist != '':
        print("%s kachal!" % (d[word]), end=' ')
    else:
        print("kachal!", end=' ')
print()
