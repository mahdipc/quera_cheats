alphabet = ['_', '*', '#', '$']


def InvalidUser(s):
    for i in s:
        if i in alphabet:
            return True
    return False


def findIP(username):
    for element in ipAndUsernames:
        if username == element[1]:
            return element[0]


def findUsername(ip):
    for element in ipAndUsernames:
        if ip == element[0]:
            return element[1]


q = int(input())
rows = [input().split() for i in range(q)]
ipDict={}
userDict={}
ipMoneyDict={}

for element in rows:
    type = element[0]
    if type == "1":
        ip, username = element[1].split(":")
        if InvalidUser(username):
            print("invalid username")
        else:
            ipDict[ip]=username
            userDict[username]=ip
            ipMoneyDict[ip]=0
    elif type == "2":
        ip, username, money = element[1].split(":")

        ipMoneyDict[ip]=ipMoneyDict[ip]-int(money)

        ipMoneyDict[userDict[username]]=ipMoneyDict[userDict[username]]+int(money)

    elif type == "3":
        ip = element[1]
        print(ipMoneyDict[ip])
