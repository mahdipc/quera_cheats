n = int(input())
first = input()
m = int(input())
second = input()
c = 0
while first[c] == second[c]:
    c += 1
print(n+m-2*c)
