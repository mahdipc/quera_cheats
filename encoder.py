from string import ascii_letters, digits


def shift(text, shift: int = 0):
    SPACE = ' '
    letters = ascii_letters + digits + SPACE
    letters_length = len(letters)

    shifted_chars = []
    for char in text:
        if char in letters: 
            shifted_chars.append(letters[(letters.index(char) + shift) % letters_length])
        else:
            shifted_chars.append(char)
    return ''.join(shifted_chars)


def swap(text):
    middle = len(text) // 2
    return text[middle:] + text[:middle]

def encode(text):
    if len(text) < 2:
        return shift(text, 7)

    for i in range(31):
        text = swap(shift(text, i))

    return text
