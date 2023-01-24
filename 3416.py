

n = int(input())


def comprese(st):
    res = []
    st += "."
    cou = 1
    for i in range(len(st)-1):
        if st[i+1] == st[i]:
            cou += 1
        else:
            res.append(st[i])
            if cou != 1:
                res.append(str(cou))

            cou = 1

    return res


def decomprese(st):
    ou = []
    nums = '0123456789'
    s = ""
    res = []
    for element in st:
        if element not in nums:
            if s != "":
                ou.append(res[-1]*(int(s)-1))
            res.append(element)
            ou.append(res[-1])
            s = ""
        else:
            s += element
    return ou


for i in range(n):
    t = int(input())
    cod = input()

    if t == 1:
        s = comprese(cod)
    elif t == 2:
        s = decomprese(cod)
    print(''.join(s))
