st = input()
r = st.count('R')
g = st.count('G')
y = st.count('Y')
if (r >= 3) or (r >= 2 and y >= 2) or (g == 0):
    print("nakhor lite")
else:
    print("rahat baash")
