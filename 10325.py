r, c = input().split()
r, c = int(r), int(c)
if c <= 10:
    print("Right", end=" ")
    print(11-r, end=" ")
    print(c)
else:
    print("Left", end=" ")
    print(11-r, end=" ")
    print(20-c+1)
