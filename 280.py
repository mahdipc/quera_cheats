a = int(input())
b = int(input())
c = int(input())
if a == 0 or b == 0 or c == 0:
    print("NO")
elif a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == a**2+b**2:
    print("YES")
else:
    print("NO")
