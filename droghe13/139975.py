def lis(arr, n):
    i, j, maxm = 0, 0, 0

    # initialize LIS values for all indexes
    lst = [1 for s in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] > arr[j] and
                    lst[i] < lst[j] + 1):
                lst[i] = lst[j] + 1

    # Pick maximum of all LIS values
    for i in range(0, n):
        if maxm < lst[i]:
            maxm = lst[i]

    return maxm


# Driver Code
n = int(input())
arr = input().split()
arr = [int(i) for i in arr]
print(lis(arr, n))

# This code is contributed
# by Mohit kumar 29
