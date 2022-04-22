t = int(input())
AA = []
BB = []
for i in range(t):
    n = int(input())
    A = input().split()
    A = [int(i) for i in A]
    AA.append([A])

    B = input().split()
    B = [int(i) for i in B]
    BB.append([B])

for i in range(t):
    br = False
    A = AA[i][0]
    B = BB[i][0]
    if len(A) != len(B):
        print("NO")
    else:
        for b in B:
            if b not in A:
                print("NO")
                br = True
                break
        if br == False:
            print("YES")
