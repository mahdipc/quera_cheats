x = input()
ss = []
lnx = len(x)
for i in range(lnx):
    for j in range(lnx):
        s = list(x)
        s1 = s.copy()
        s1[i], s1[j] = s[j], s[i]
        print(''.join(s1), end=" ")
        # if s[0] == '0' or (int(''.join(s)) in ss):
        #     continue
        # print(''.join(s), end=' ,')
        # ss.append(int(''.join(s)))
    print()

# is_break = False
# ss.sort()
# print(ss)
# for i in range(len(ss)):
#     if ss[i] == int(''.join(x)) and i != len(ss)-1:
#         print(ss[i+1])
#         is_break = True
#         break
# if is_break == False:
#     print(0)
