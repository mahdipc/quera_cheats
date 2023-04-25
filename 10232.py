
n, l = map(int, input().split())

covered_distance = 0
total_duration = 0
for i in range(n):
    distance, red_duration, green_duration = map(int, input().split())

    total_duration += distance - covered_distance
    covered_distance = distance

    cycle = red_duration + green_duration
    remain = total_duration % cycle
    if remain < red_duration:
        total_duration += red_duration - remain

total_duration += l - covered_distance
print(total_duration)
