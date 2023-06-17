days_in_month = {
    'Farvardin': 31,
    'Ordibehesht': 31,
    'Khordad': 31,
    'Tir': 31,
    'Mordad': 31,
    'Shahrivar': 31,
    'Mehr': 30,
    'Aban': 30,
    'Azar': 30,
    'Dey': 30,
    'Bahman': 30,
    'Esfand': 29
}
day_name=["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe" ,"jome"]



T=int(input())
for i in range(T):
    day,month,week_name=input().split()
    day_request,month_request=input().split()
