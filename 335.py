strs = input()
i = 1
while '{' in strs:
    for iend, st in enumerate(strs):
        if st == '}':
            break

    for istart in range(iend, -1, -1):
        if strs[istart] == '{':
            break
    res = sum(map(int, strs[istart+1:iend].split(',')))
    print(res)
    strs = strs[:istart]+str(res)+strs[iend+1:]
    i += 1
