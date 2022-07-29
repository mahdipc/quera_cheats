a, b = input().split()
a, b = int(a), int(b)

h, m = (12-a) % 12, (60-b) % 60
print(f'{h:02}:{m:02}')
