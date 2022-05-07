def find(num1, num2, num3):
    res = [num1, num2, num3]
    for i in range(1, 5):
        if i not in res:
            return i
