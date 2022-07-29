n, m = input().split()
n, m = int(n), int(m)
matrix = [input().split() for i in range(n)]
matrix = [[int(j) for j in i] for i in matrix]
counts = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        s = matrix[i][j]
        if matrix[i+1][j] > s and matrix[i-1][j] > s and matrix[i][j+1] < s and matrix[i][j-1] < s:
            counts += 1
        elif matrix[i+1][j] < s and matrix[i-1][j] < s and matrix[i][j+1] > s and matrix[i][j-1] > s:
            counts += 1
print(counts)
