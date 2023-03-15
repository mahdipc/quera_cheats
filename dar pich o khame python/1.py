def calculate_floor(acts):
    c = 0
    for a in acts:
        if a == "U":
            c += 1
        elif a == "D":
            c -= 1
    return c
