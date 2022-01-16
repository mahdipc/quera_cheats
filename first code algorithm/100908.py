import numpy as np


n, m, q = input().split()
n, m, q = int(n), int(m), int(q)
days_import = [
    'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]
days_import = np.array(days_import)

# st_data = []
# for i in range(n):
#     st_n = input().split()
#     st_data.append(st_n)
st_data = [input().split() for i in range(n)]
st_data = np.array(st_data)
# exep = []
# for i in range(m):
#     # st_n=input()
#     st_n = input().split()
#     exep.append(st_n)
exep = [input().split() for i in range(m)]

exep = np.array(exep)
# time_counsomers = []
# for i in range(q):
#     # st_n=input()
#     st_n = input()
#     time_counsomers.append(st_n)
time_counsomers = [input() for i in range(q)]
time_counsomers = np.array(time_counsomers, dtype=np.datetime64)


def day_of_week_num(dts):
    return days_import[(dts.astype('datetime64[D]').view('int64') - 4) % 7]


def convert_time_to_secend(times):
    res = []
    for time in times:
        ddd = time.split(':')
        res.append(int(ddd[0])*60+int(ddd[1]))
    res = np.array(res)
    return res


def Is_res_piorr(pioors):
    isOk = False
    for pioor in pioors:
        if (time_counsomer > np.datetime64(pioor[1])) & (time_counsomer < np.datetime64(pioor[2])) & (pioor[3] == 'open'):
            print('true')
            isOk = True
            break
    return isOk


data_exep = np.array(exep[:, 1:3], dtype=np.datetime64)

# time_counsomer=time_counsomers[1]
for time_counsomer in time_counsomers:

    res_s = exep[(time_counsomer < data_exep[:, 1]) &
                 (time_counsomer > data_exep[:, 0])]
    days = np.array(days)
    if res_s.shape[0] == 0:
        week_time = day_of_week_num(time_counsomer)
        day_posibels = st_data[st_data[:, 0] == week_time]
        time_day_counsomer = convert_time_to_secend(
            [str(time_counsomer[0]).split('T')[1]])
        for day_posibel in day_posibels:
            startend_time = convert_time_to_secend(day_posibels[0, 1:])
            if (startend_time[0] < time_day_counsomer) & (startend_time[1] > time_day_counsomer):
                print('true')
                break
        print('false')

    else:
        res_Tenants = res_s[res_s[:, 0] == 'Tenant']
        isOk = Is_res_piorr(res_Tenants)
        if isOk == False:
            res_Stores = res_s[res_s[:, 0] == 'Store']
            isOk = Is_res_piorr(res_Stores)
            if (isOk == False):
                res_Stations = res_s[res_s[:, 0] == 'Station']
                isOk = Is_res_piorr(res_Stores)
        if isOk == False:
            print('false')
