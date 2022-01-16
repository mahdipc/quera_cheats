st = input()

min_st = int(input())
max_st = int(input())


def split(word):
    return [int(char) for char in word]


MyList = split(st)


def partition(num):
    def backtrack(index, chosen):
        if index == len(num):
            st.append(1)
        else:
            for i in range(index, len(num)):
                cur = num[index:i + 1]
                val_cur = int("".join(map(str, cur)))
                if (val_cur >= min_st) & (val_cur <= max_st) & (cur[0] > 0):
                    chosen.append(cur)
                    backtrack(i + 1, chosen)
                    chosen.pop()
    backtrack(0, [])


st = []
partition(MyList)
print(len(st))
