
def myPow(base, exp):
    if exp == 0:
        return 1.0
    elif exp % 2 == 0:
        temp = myPow(base, exp // 2)
        return temp * temp
    else:
        temp = myPow(base, (exp - 1) // 2)
        return base * temp * temp


if __name__ == "__main__":
    base = float(input())
    exp = int(input())
    result = myPow(base, exp)
    print("{:.3f}".format(result))
