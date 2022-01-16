n = int(input())
M = [int(j) for j in input().split()]
KH = [int(j) for j in input().split()]

k = int(input())
KHman = []
Mman = []
while ((M != []) | (k != 0)):

    choose, i = max(M), M.index(M)
    M.remove(choose)
    if (KH[i] > min(KHman)) | (M == []):
        k = k-1
        Mman.append(choose)
        KHman.append(KH[i])


print(sum(Mman)*min(KHman))
