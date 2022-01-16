import numpy as np
first = input().split()
secend = input().split()
first = [int(i) for i in first]
secend = [int(i) for i in secend]


def shift(seq, n):
    return seq[n:]+seq[:n]


def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)


flag = 0
for i in range(5):
    for j in range(5):
        res = (np.array(first[1:4])+np.array(secend[1:4])) % 10
        if (convert(res) % 6) == 0:
            print("Boro joloo :)")
            flag = 1
            break

        secend = shift(secend, 1)
    first = shift(first, 1)

    if(flag == 1):
        break

if flag == 0:
    print("Gir oftadi :(")
