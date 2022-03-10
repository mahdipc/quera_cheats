n = int(input())
copens = [input() for i in range(n)]


for copen in copens:
    revers_copen = list(copen[::-1])
    for indx, char in enumerate(revers_copen):
        res = list(revers_copen[:indx+1])
        res.sort()
        if res == revers_copen[:indx+1]:
            continue
        else:
            revers_copen[:indx+1] = res
            break
    new_copen = "".join(revers_copen[::-1])
    if new_copen == copen:
        print("no answer")
    else:
        print(new_copen)
