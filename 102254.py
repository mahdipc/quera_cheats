n = input()
list_n = [int(x) for x in n]

all_list_n = ["".join(map(str, list_n))]
while True:
    dict = {i: list_n.count(i) for i in list_n}
    list_n = list(dict.keys())
    for i in dict.values():
        if i != 1:
            list_n.append(i)

    list_n.sort()
    if "".join(map(str, list_n)) in all_list_n:
        break
    all_list_n.append("".join(map(str, list_n)))
print(all_list_n[-1])
