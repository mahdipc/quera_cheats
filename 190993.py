n, q, l = input().split()
n, q, l = int(n), int(q), int(l)

list_ = {}
for i in range(n):
    st = input().split()
    list_[st[0]] = st[1]

for i in range(q):
    try:
        print(list_[input()])
    except:
        print("Unknown")
