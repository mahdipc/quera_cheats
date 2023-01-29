n = int(input())
st = [int(input()) for i in range(n)]
val = ["B", "KiB", "MiB", "GiB", "TiB"]

for item in st:
    res = item//1024
    state = 0
    while res > 0:
        res = res//1024
        state += 1
    print(item//(1024**state), val[state], sep="")
