a, b, c, d, e, f = tuple(map(int, input().split()))
A = [a, b]
B = [d, e, f]
C = [[ai >= bi for bi in B] for ai in A]
for cc in C:
    if sum(cc) >= 2:
        print("zende mimuni")
        break
else:
    print("dari mimiri")
