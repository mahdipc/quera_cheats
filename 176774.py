fingers_per_hand = int(input().strip())
hands = int(input().strip())
a = int(input().strip())
b = int(input().strip())

F = fingers_per_hand * hands
total = a + b

if F == 0:
    print(0)
else:
    r = total % F
    if r == 0:
        print(0 if total == 0 else F)
    else:
        print(r)
