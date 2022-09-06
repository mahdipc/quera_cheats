n = input()
s = [int(j) for j in input().split()]
marker = dict((x, s.count(x)) for x in set(s))
min_marker_number = min(marker.values())
rrr = list(marker.keys())
rrr.sort()
for ind in rrr:

    if marker[ind] == min_marker_number:
        print(ind)
        break
