def is_magical_binary_number(num):
    # Convert the number to decimal, hexadecimal and binary string
    decimal_str = str(num)
    hexadecimal_str = hex(num)[2:]
    binary_str = bin(num)[2:]

    # Check if the number satisfies at least two of the conditions
    count = 0
    if decimal_str == decimal_str[::-1]:
        count += 1
    if hexadecimal_str == hexadecimal_str[::-1]:
        count += 1
    if binary_str == binary_str[::-1]:
        count += 1
    return count >= 2
T = int(input())
for i in range(T):
    num = int(input())
    if is_magical_binary_number(num):
        print("Magical")
    else:
        print("I'm sorry Sherlock :(")