x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())
d_V = v2-v1
d_X = x2-x1
if d_V == 0:
    print("WAIT WAIT")
elif d_X/d_V > 0:
    print("BORO BORO")
else:
    print("SEE YOU")
