n = input()
st = input().split()
for s in st:
    num = int(s)
    if num > 3:
        print('*')
    else:
        print('*'*num)
