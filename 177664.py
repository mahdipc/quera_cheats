n=int(input())
max=0
best_name=""
for _ in range(n):
    name,value=input().split()
    value=int(value)
    if value>max:
        max=value
        best_name=name
print(best_name)
        
    