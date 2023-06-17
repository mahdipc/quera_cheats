st = input()
all_patter = []


def replace_patt(st):
    if '?' not in st:
        all_patter.append(st)
    else:
        ind = st.index('?')
        replace_patt(st[:ind] + '0' + st[ind+1:])
        replace_patt(st[:ind] + '1' + st[ind+1:])


replace_patt(st)
all_patter.sort()
[print(i) for i in all_patter[::-1]]
