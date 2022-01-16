st=input()
def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return value.strip()
def eq(ABC):
    t=''
    sts=ABC.split('#')
    if (ABC=="#"):
        t=res
    elif  (sts[0]!='') & (sts[1]=='') & (sts[0]+res[len(sts[0]):]==res):
        t=res[len(sts[0]):]
    elif  (sts[1]!='') & (sts[0]=='') & (res[:-len(sts[1])]+sts[1]==res):
        t=res[:-len(sts[1])]
    elif (sts[1]!='') & (sts[0]!=''):
        if sts[0]+res[len(sts[0]):-len(sts[1])]+sts[1]==res:
            t=res[len(sts[0]):-len(sts[1])]
    return t
A,B,C=st.replace('+','=').split('=')
A,B,C=intTryParse(A),intTryParse(B),intTryParse(C)

if type(A)==str:
    res=str(C-B)
    t=eq(A)
    re=st.replace('#',t)
elif type(B)==str:
    res=str(C-A)
    t=eq(B)
    re=st.replace('#',t)
else:
    res=str(A+B)
    t=eq(C)
    re=st.replace('#',t)

if t=='':
    print(-1)
else:
    print(re)
    