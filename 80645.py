n = int(input())
m = int(input())
a = int(input())
b = int(input())


def ceil_div(x, y):
    return (x + y - 1) // y


vertical_sweeps = min(ceil_div(m, a), ceil_div(m, b))
horizontal_sweeps = min(ceil_div(n, a), ceil_div(n, b))

print(min(vertical_sweeps, horizontal_sweeps))
