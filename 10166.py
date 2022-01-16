n=int(input())
st=input()
len_st=n//6+1
keyv=('331122'*len_st)[:n]
nezam=('123123'*len_st)[:n]
shir=('212312'*len_st)[:n]
sum_barare={'keyvoon':0,'nezam':0,'shir farhad':0}
for i in range(n):
    sum_barare['keyvoon']+=int(keyv[i]==st[i])
    sum_barare['nezam']+=int(nezam[i]==st[i])
    sum_barare['shir farhad']+=int(shir[i]==st[i])
sort_orders =sorted(sum_barare.items(), key=lambda x: x[1], reverse=True)
print(sort_orders[0][1])
for i in sort_orders:
	print(i[0])