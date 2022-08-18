

n = int(input())
arr = input().split()
arr = [int(i) for i in arr]

for i in range(1, n-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print('Ey baba :(')
        break
else:
    print('Bah Bah! Ajab jooji!')
