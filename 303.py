n1 = int(input())
n2 = int(input())


def show_fib_nth(n1, n2):
    if n2 == 1:
        print(n1)
    else:
        print(n1)
        show_fib_nth(n2-n1, n1)


show_fib_nth(n1, n2)
