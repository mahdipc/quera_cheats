n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())


def is_between(a, x, b):
    if b < a:
        b += n
    if x < a:
        x += n
    return a < x < b


share_vertex = (a == c) or (a == d) or (b == c) or (b == d)
cross_inside = (is_between(a, c, b) != is_between(a, d, b)) and (not share_vertex)

print(4 if cross_inside else 3)
