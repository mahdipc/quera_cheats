n = int(input())

lights = [int(input()) for i in range(n)]
s = lights[0]
count = 0

for light in lights[1:]:
    if s != light:
        count += 1
        s = light
print(count)
