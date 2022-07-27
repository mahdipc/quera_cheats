def xorOfArray(arr):
    n = len(arr)
    xor_arr = 0
    for i in range(n):
        xor_arr = xor_arr ^ arr[i]

    return xor_arr


n = int(input())
arrs = list(map(int, input().split()))
uniqe_code = []
for arr in arrs:
    if arrs.count(arr) == 1:
        uniqe_code.append(arr)
print(xorOfArray(uniqe_code))
