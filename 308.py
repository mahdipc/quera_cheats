import string


st = input().strip().lower()
alphabet=string.ascii_letters + string.digits
st = ''.join([i for i in st if i in alphabet])
if st == st[::-1]:
    print("YES")
else:
    print("NO")
