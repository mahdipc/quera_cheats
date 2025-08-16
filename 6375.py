a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
s = a + b + c

if a == b == c:
    print(0)
elif 3 * a == s or 3 * b == s or 3 * c == s:
    print(1)
else:
    print(2)
