
a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2 - 4 * a * c)

if a != 0:
    if delta == 0:
        x = (-b) / (2 * a)
        x_string = str(x) + "000"
        int_string = str(int(x)) if x >= 0 else "-" + str(int(x))
        x = int_string + \
            (x_string[x_string.index("."):x_string.index(".") + 4])
        print(x)
    elif delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x1_string = str(x1) + "000"
        int_string1 = str(int(x1)) if x1 >= 0 else "-" + str(int(x1))
        x1 = int_string1 + \
            (x1_string[x1_string.index("."):x1_string.index(".") + 4])

        x2 = (-b - (delta ** 0.5)) / (2 * a)
        x2_string = str(x2) + "000"
        int_string2 = str(int(x2)) if x2 >= 0 else "-" + str(int(x2))
        x2 = int_string2 + \
            (x2_string[x2_string.index("."):x2_string.index(".") + 4])

        print("%s\n%s" % (x1, x2) if x1 < x2 else "%s\n%s" % (x2, x1))
    else:
        print("IMPOSSIBLE")
else:
    if b != 0:
        x = -c / b
        x_string = str(x) + "000"
        int_string = str(int(x)) if x >= 0 else "-" + str(int(x))
        x = int_string + \
            (x_string[x_string.index("."):x_string.index(".") + 4])
        print("%s" % x)
    else:
        print("IMPOSSIBLE")
