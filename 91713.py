n = int(input())
numbers = [input() for i in range(n)]


def have_4_number_duplicate(number):
    for n in number:
        if number.count(n) >= 4:
            return True
    return False


def sequence_value(number):
    for i in range(6):
        if number[i] == number[i+1] and number[i] == number[i+2]:
            return True
    return False


for number in numbers:
    if number == number[::-1] or sequence_value(number) or have_4_number_duplicate(number):
        print("Ronde!")
    else:
        print("Rond Nist")
