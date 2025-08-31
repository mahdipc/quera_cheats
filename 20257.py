k, a, b = input().split()
k, a, b = int(k), int(a), int(b)


def best_time(k: int, a: int, b: int) -> int:
    if a == b:
        return 0
    ans = abs(a - b)

    a_floor = (a // k) * k
    a_ceil = -((-a) // k) * k
    b_floor = (b // k) * k
    b_ceil = -((-b) // k) * k

    candidates_a = {a_floor, a_ceil}
    candidates_b = {b_floor, b_ceil}

    for m1 in candidates_a:
        for m2 in candidates_b:
            cost = abs(a - m1) + abs(m1 - m2) // k + abs(b - m2)
            if cost < ans:
                ans = cost

    return ans


print(best_time(k, a, b))
