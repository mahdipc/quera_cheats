k = int(input())
password = input()
safe_box = [input() for i in range(k)]
count = 0
for i in range(k):
    char = password[i]
    n = safe_box[i].index(char)
    if n > len(safe_box[i])-n:
        n = len(safe_box[i])-n
    count += n

print(count)
