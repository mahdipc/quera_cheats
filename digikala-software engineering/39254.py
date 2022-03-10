n = int(input())
st = [input().split() for i in range(n)]
init_area = int(input())
final_area = int(input())


def isContain(i):
    for item in st:
        if i >= int(item[0]) and i <= int(item[1]):
            return True
    return False


contain = True
for i in range(init_area, final_area+1):
    if not isContain(i):
        print("false")
        contain = False
        break
if contain:
    print("true")
