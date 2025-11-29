t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    need = [0] * 26 

    for _ in range(n):
        s = input().strip()
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for i in range(26):
            if cnt[i] > need[i]:
                need[i] = cnt[i]

    print(sum(need))
