n = int(input())
k = int(input())
p = int(input())
q = int(input())

if n-k == p-q:
    print("Equal")
elif n-k > p-q:
    print("Shekarestan")
else:
    print("Namakestan")
