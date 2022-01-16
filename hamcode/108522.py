import numpy as np
n, k = map(int, input().split())
mashkook = [input() for i in range(n)]
mamad = [input() for i in range(k)]


def compareA(s1, s2):
    for j in range(len(s2)):
        res_str = ''.join([s2[i] for i in range(len(s2)) if i != j])

        if s1 == res_str:
            return True
    return False


def compareB(s1, s2):
    if s1 == s2:
        return True
    for j in range(len(s2)):
        res_str2 = ''.join([s2[i] for i in range(len(s2)) if i != j])
        res_str1 = ''.join([s1[i] for i in range(len(s1)) if i != j])

        if res_str2 == res_str1:
            return True
    return False


def check(mashk, mam):
    A = [mam, mashk]
    n_s1 = len(mashk)
    n_s2 = len(mam)
    if n_s1 < n_s2:
        A = [mashk, mam]
        n_s1, n_s2 = n_s2, n_s1
    if mashk.lower() == mam.lower():
        return True
    if n_s1-n_s2 == 1:
        return compareA(A[0], A[1])
    if n_s2 == n_s1:
        return compareB(A[0], A[1])
    return False


item = 0
for mash in mashkook:
    A = []
    for m in mamad:
        if check(mash, m):
            A.append(1)
        else:
            A.append(0)

    item = item+np.array(A)
for i in item:
    print(i)
