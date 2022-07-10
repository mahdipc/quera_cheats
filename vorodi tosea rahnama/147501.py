n = int(input())
temp_days = input().split()
for temp_day in temp_days:
    if int(temp_day) <= 15:
        print('heater')
    else:
        print('cooler')
