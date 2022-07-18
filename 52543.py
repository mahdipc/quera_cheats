n = int(input())
st = input().split()
st = list(map(int, st))
st.sort()
while len(st) > 0:
    print(st.pop(), end=' ')
    if len(st)==0:
        break
    print(st.pop(0), end=' ')
