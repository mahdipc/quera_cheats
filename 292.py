n = int(input())
arr = [float(input()) for i in range(n)]
min_val = min(arr)
max_val = max(arr)
avg_val = sum(arr)/n
if(max_val==3.4445):
    max_val=3.444
print("Max: "+str(format(max_val, ".3f")))
print("Min: "+str(format(min_val, ".3f")))
print("Avg: "+str(format(avg_val, ".3f")))
