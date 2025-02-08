import re

s = input()

p = re.compile(r"(kalan(\s*)tar)")
result_st = []
while True:
    ma = list(p.finditer(s))
    if not ma:
        break
    t = 0
    c = 0
    prt = []
    last = 0
    for m in ma:
        start, end = m.span()
        prt.append(s[last:start])
        spaces = m.group(2)
        if len(spaces) == 0:
            t += 1
        else:
            c += 1
        last = end
    prt.append(s[last:])
    s = "".join(prt)
    result_st.append((t, c))

print(len(result_st))
for x, y in result_st:
    print(x, y)
