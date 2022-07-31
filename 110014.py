s = []
s.append(input().split())
s.append(input().split())
if s[0][0] == s[0][1] or \
        s[0][0] == s[1][1] or \
        s[1][0] == s[1][1] or \
        s[1][0] == s[0][1]:
    print('YES')
else:
    print('NO')
