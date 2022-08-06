e = input().split()
e = [int(i) for i in e]

if e[4]*e[2]+e[0] >= e[4]*e[3]+e[1]:
    if e[4]*e[2] >= e[4]*e[3]:
        print('Eyval baba!')
    else:
        print('Naaa, eshtebahe!')
elif e[4]*e[2] <= e[4]*e[3]:
    print('Eyval baba!')
else:
    print('Naaa, eshtebahe!')
