st = input()


def rull_tir(pls, mins):
    pls.sort()
    pls = pls[::-1]
    mins.sort()
    reg = rull_first(pls, mins[:len(pls)])
    bedoneEdalat = mins[len(pls):]
    addadeEdalat = eval(reg)

    if(addadeEdalat < 0):
        reg += "+"+str(bedoneEdalat[-1])
        bedoneEdalat.pop()

    for i in range(len(bedoneEdalat)):
        reg += "-"+str(bedoneEdalat[i])

    return reg


def rull_sec(pls, mins):
    pls.sort()
    pls = pls[::-1]
    mins.sort()
    reg = rull_first(pls[:len(mins)], mins)

    bedoneEdalat = pls[len(mins):]
    addadeEdalat = eval(reg)
    if(bedoneEdalat[0] > addadeEdalat):
        bedoneEdalat[0] = -bedoneEdalat[0]

    for i in range(len(bedoneEdalat)):
        reg += "+"+str(bedoneEdalat[i])

    return reg


def rull_first(pls, mins):
    pls.sort()
    pls = pls[::-1]
    mins.sort()
    reg = ""
    for i in range(len(pls)):
        reg += "+"+str(pls[i])+"-"+str(mins[i])
    return reg


s = ""
flag_plus = 0
flag_min = 0
pls = []
mins = []
for i in st:
    if(i == "+"):
        if(flag_plus == 1):
            if s != "":
                pls.append(int(s))
            s = ""
        else:
            if s != "":
                mins.append(int(s))
            s = ""

        flag_plus = 1
        flag_min = 0
    elif (i == "-"):
        if(flag_min == 1):
            if s != "":
                mins.append(int(s))
            s = ""
        else:
            if s != "":
                pls.append(int(s))
            s = ""
        flag_min = 1
        flag_plus = 0
    else:
        s += i

if(flag_min == 1):
    mins.append(int(s))
    s = ""
else:
    pls.append(int(s))
    s = ""

reg = ""
if len(pls) == len(mins):
    reg = rull_first(pls, mins)
    print(reg+"="+str(eval(reg)))
elif len(pls) > len(mins):
    reg = rull_sec(pls, mins)
    print(reg+"="+str(eval(reg)))
elif len(pls) < len(mins):
    reg = rull_tir(pls, mins)
    print(reg+"="+str(eval(reg)))
