n = int(input())


def dicSplit(arr, item):
    arrs = arr.split(",")
    for element in arrs:
        var, id = element.split(':')
        if var.strip() == item:
            return int(id)


def arrSplit(arr, item):
    item = int(item)
    return int(arr[1:-1].split(',')[item])


prints = {}
operators = {}
for i in range(n):
    s = input()
    if 'print' in s:
        var, id = s[6:].split('[')
        prints[var.strip()] = id[:-1].strip()
    else:
        var, id = s.split(':=')
        operators[var.strip()] = id.strip()
for p in prints:
    o = operators[p]
    if o[0] == '[':
        print(arrSplit(o, prints[p]))
    else:
        print(dicSplit(o, prints[p]))

# print(prints)
# print(operators)
