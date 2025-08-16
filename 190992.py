h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

diff = t2 - t1
if diff <= 0:  # شامل حالت مساوی هم می‌شود
    diff += 24 * 3600

H = diff // 3600
M = (diff % 3600) // 60
S = diff % 60

print(f"{H:02d}:{M:02d}:{S:02d}")
