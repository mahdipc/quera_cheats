import numpy as np


def res8():
    return [10000000, 10000001, 10000010, 10000011, 10000100, 10000101, 10000110, 10000111, 10001000, 10001001, 10001010, 10001011, 10001100, 10001101, 10001110, 10001111, 10010000, 10010001, 10010010, 10010011, 10010100, 10010101, 10010110, 10010111, 10011000, 10011001, 10011010, 10011011, 10011100, 10011101, 10011110, 10011111, 10100000, 10100001, 10100010, 10100011, 10100100, 10100101, 10100110, 10100111, 10101000, 10101001, 10101010, 10101011, 10101100, 10101101, 10101110, 10101111, 10110000, 10110001, 10110010, 10110011, 10110100, 10110101, 10110110, 10110111, 10111000, 10111001, 10111010, 10111011, 10111100, 10111101, 10111110, 10111111, 11000000, 11000001, 11000010, 11000011, 11000100, 11000101, 11000110, 11000111, 11001000, 11001001, 11001010, 11001011, 11001100, 11001101, 11001110, 11001111, 11010000, 11010001, 11010010, 11010011, 11010100, 11010101, 11010110, 11010111, 11011000, 11011001, 11011010, 11011011, 11011100, 11011101, 11011110, 11011111, 11100000, 11100001, 11100010, 11100011, 11100100, 11100101, 11100110, 11100111, 11101000, 11101001, 11101010, 11101011, 11101100, 11101101, 11101110, 11101111, 11110000, 11110001, 11110010, 11110011, 11110100, 11110101, 11110110, 11110111, 11111000, 11111001, 11111010, 11111011, 11111100, 11111101, 11111110, 11111111]


def res71():
    return [1000000, 1000001, 1000010, 1000011, 1000100, 1000101, 1000110, 1000111, 1001000, 1001001, 1001010, 1001011, 1001100, 1001101, 1001110, 1001111, 1010000, 1010001, 1010010, 1010011, 1010100, 1010101, 1010110, 1010111, 1011000, 1011001, 1011010, 1011011, 1011100, 1011101, 1011110, 1011111]


def res72():
    return [1100000, 1100001, 1100010, 1100011, 1100100, 1100101, 1100110, 1100111, 1101000, 1101001, 1101010, 1101011, 1101100, 1101101, 1101110, 1101111, 1110000, 1110001, 1110010, 1110011, 1110100, 1110101, 1110110, 1110111, 1111000, 1111001, 1111010, 1111011, 1111100, 1111101, 1111110, 1111111]


def res6():
    return [100000, 100001, 100010, 100011, 100100, 100101, 100110, 100111, 101000, 101001, 101010, 101011, 101100, 101101, 101110, 101111, 110000, 110001, 110010, 110011, 110100, 110101, 110110, 110111, 111000, 111001, 111010, 111011, 111100, 111101, 111110, 111111]


n = input()
len_n = len(n)
intn = int(n)
max_1 = int(len_n*'1')
if intn >= max_1:
    s = (2**(len_n))-1
else:
    s = (2**(len_n-1))-1
    if len_n >= 8:
        for i in res8():
            if i <= intn:
                s += 1

    elif len_n == 7:
        if intn < 1100000:
            for i in res71():
                if i <= intn:
                    s += 1
        else:
            s += 32
            for i in res72():
                if i <= intn:
                    s += 1
    elif len_n == 6:
        for i in res6():
            if i <= intn:
                s += 1
    else:
        b = {'0', '1'}
        for i in range(10**(len_n-1), intn+1):
            t = set(str(i))
            if b == t or t == {'0'} or t == {'1'}:
                s += 1

print(s)