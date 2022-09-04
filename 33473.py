

def get_func(ls):

    def square(x):
        return x**2

    def circle(x):
        return (3.141592653589793)*(x**2)

    def rectangle(x, y):
        return x*y

    def triangle(x, y):
        return 0.5*x*y
    s = []
    for item in ls:
        s.append(locals()[item])
    return s
