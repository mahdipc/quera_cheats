nm = input().split()
A = []
B = []
for i in range(int(nm[0])):
    A.append([int(i) for i in input().split()])
for i in range(int(nm[1])):
    B.append([int(i) for i in input().split()])

C = []
for i in range(int(nm[0])):
    C.append([])
    keep = []
    for j in range(int(nm[2])):
        keep.append(0)
    C[i] = keep

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

for r in C:
    print(" ".join([str(i) for i in r]))
