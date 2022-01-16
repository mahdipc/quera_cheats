n = input()
while int(n) >= 10:
    n = sum(int(digit) for digit in str(n))
print(n)
