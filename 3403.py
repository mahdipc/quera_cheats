s = [int(input()) for i in range(4)]
sum = 0
prod = 1
for i in s:
    sum += i
    prod *= i
print("Sum :", f"{sum:.6f}")
print("Average :", f"{sum/4:.6f}")
print("Product :", f"{prod:.6f}")
print("MAX :", f"{max(s):.6f}")
print("MIN :", f"{min(s):.6f}")
