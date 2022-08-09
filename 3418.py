def gcd(arr, n):

    high = max(arr)

    count = [0] * (high + 1)
    for i in range(0, n):
        count[arr[i]] += 1

    counter = 0

    for i in range(high, 0, -1):
        j = i

        while (j <= high):

            if (count[j] > 0):
                counter += count[j]

            j += i

            if (counter == 2):
                return i
        counter = 0


n = int(input())
arr = input().split()
arr = [int(i) for i in arr]

print(gcd(arr, n))
