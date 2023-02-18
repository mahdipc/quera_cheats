t, a, b = map(int, input().split())

c = a + b + 2
m_c = int(t / (a + b + 2))

n_arr = m_c
n_mom = m_c

remain = t % c
if remain > 0:
    n_arr += 1
if remain - 1 - a > 0:
    n_mom += 1

print(n_arr, n_mom)
