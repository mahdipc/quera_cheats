n = input()
s = [int(j) for j in input().split()]
dict((x, s.count(x)) for x in set(s))
