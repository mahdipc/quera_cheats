T = input()
n = int(input())
ss = [input() for i in range(n)]
count = 0
for item in ss:
    if T in item:
        count += 1
print(count)
