st = input()
word = []
for l in st:
    if l == '=' and len(word) > 0:
        word.pop()
    elif l == '=' and len(word) == 0:
        continue
    else:
        word.append(l)

print(''.join(word))
