import sys
import functools
import collections


@functools.lru_cache(None)
def subSolve(x, y, u, v, changes):
    if x > y or u > v:
        return 0
    if changes < 0:
        return -(10**9)
    result = 0
    result = max(result, subSolve(x + 1, y, u, v, changes))
    result = max(result, subSolve(x, y - 1, u, v, changes))
    result = max(result, subSolve(x, y, u + 1, v, changes))
    result = max(result, subSolve(x, y, u, v - 1, changes))
    if x == y and u == v:
        cost = 0 if S[x] == T[u] else 1
        if cost <= changes:
            result = max(result, 1)
    if x < y and u < v:
        chars = [S[x], S[y], T[u], T[v]]
        cnt = collections.Counter(chars)
        cost = len(chars) - max(cnt.values())
        if cost <= changes:
            result = max(
                result, 2 + subSolve(x + 1, y - 1, u + 1, v - 1, changes - cost)
            )
    return result


sys.setrecursionlimit(10**7)

k = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

n, m = len(S), len(T)

print(subSolve(0, n - 1, 0, m - 1, k))
