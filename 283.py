a, b = int(input()), int(input())

if b >= a:
    print("Wrong order!")
elif (b - a) % 2 != 0:
    print("Wrong difference!")
else:
    c = a - b
    master_layer = ("* " * a + "\n") * (c // 2)
    middle_start = ("* " * (c // 2) + "  " * b + "* " * (c // 2) + "\n") * b
    print(f'{master_layer}{middle_start}{master_layer[:-1]}')