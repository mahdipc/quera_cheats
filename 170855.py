import math
T = int(input())
for i in range(T):
    table_diameter, pizza_width, pizza_length = input().split()
    pizza_length, pizza_width, table_diameter = int(
        pizza_length), int(pizza_width), int(table_diameter)
    pizza_diagonal = math.sqrt(pizza_length**2 + pizza_width**2)

    pizza_radius = pizza_diagonal / 2

    # compare pizza diameter with table diameter
    if pizza_diagonal <= table_diameter*2:
        print("Pizza fits on the table.")
    else:
        print("Pizza does not fit on the table.")
