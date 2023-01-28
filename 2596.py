
def can_valid(number, st):
    for divisor in st:
        if number % divisor != 0:
            return False
    return True


q = int(input())
st = input().split()
st = [int(i) for i in st]
st.sort()
count = 0
for i in range(1, 1001):
    if can_valid(i, st):
        count += 1

print(count)
