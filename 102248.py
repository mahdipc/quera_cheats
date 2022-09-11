def compare(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    while True:
        if len(string1) == 0 or len(string2) == 0:
            break
        if string1[0] == string2[0]:
            string1.pop(0)
            string2.pop(0)
        elif string1[0] > string2[0]:
            string2.pop(0)
        else:
            string1.pop(0)
        string1 = string1[::-1]
        string2 = string2[::-1]
    res = ''.join((string1+string2)[::-1])
    if res == '':
        res = 'Both strings are empty!'
    return res
