flag = 0
sts = [input() for i in range(5)]
for i in range(5):
    st = sts[i]
    if ("MOLANA" in st) | ("HAFEZ" in st):
        print(i+1, end=' ')
        flag = 1
if flag == 0:
    print("NOT FOUND!")
