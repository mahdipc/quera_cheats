def change_char_to_number(i):
    if i == 'A':
        return 0
    if i == 'B':
        return 1
    if i == 'C':
        return 2
    if i == 'D':
        return 3


n = int(input())
S = input()
S = [change_char_to_number(i) for i in S]
k = int(input())
# answer_sheet=[input() for i in range(n*k)]

for i in range(k):
    sum = 0
    for j in range(n):
        answer_sheet = input()
        if '#' not in answer_sheet:
            sum += 0
        elif answer_sheet.count('#') > 1:
            sum += -1
        elif answer_sheet[S[j]] == '#':
            sum += 3
        else:
            sum += -1
    print(sum)
