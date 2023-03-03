n = int(input())
count = sum(all(c in {'0', '1'} for c in str(i)) for i in range(1, n+1))
print(count)


count = 2**bin(n)[2:].count('1') - (n % 2 == 0)
print(count-1)
