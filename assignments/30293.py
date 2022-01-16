st = input()


def split(word):
    return [int(char) for char in word]


MyList = split(st)
while(True):
    my_dict = {i: MyList.count(i) for i in MyList}
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    values = [i for i in values if i != 1]

    MyList0 = values+keys

    # MyList0.sort()
    if MyList == MyList0:
        break
    MyList = MyList0
print("".join(map(str, MyList)))
