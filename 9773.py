n = int(input())
for i in range(1, n+1, 2):
    print(((n-i)//2)*' '+i*'*'+((n-i)//2)*' ' +
          ((n-i)//2)*' '+i*'*'+((n-i)//2)*' ')
for i in range(n-2, 0, -2):
    print(((n-i)//2)*' '+i*'*'+((n-i)//2)*' ' +
          ((n-i)//2)*' '+i*'*'+((n-i)//2)*' ')
