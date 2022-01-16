def IsUserExist(userName):
    if not userName in sta_registerUserName:
        print('No Such User Found!')
        return False
    return True


def REGISTER(userName, timeStemp):
    if not userName in sta_registerUserName:
        sta_registerUserName.append(userName)
        sta_registerTimeStemp.append(timeStemp)
        print('Registered Successfully')
    else:
        print('Duplicate User!')


def howMochAmount(userName):
    return np.sum(np.array([i[1] for i in sta_registerAmount if i[0] == userName]))


def DEPOSIT(userName, amount, timeStemp):
    if IsUserExist(userName):
        sta_registerAmount.append([userName, amount, timeStemp])
        print(howMochAmount(userName))


def WITHDRAW(userName, amount, timeStemp):
    if IsUserExist(userName):
        if amount > 200:
            print('Maximum Amount Exceeded!')
        elif howMochAmount(userName) < amount:
            print('Not Enough Fund!')
        elif ~isCoinBank(amount):
            print('Not Enough Banknotes!')
        else:
            sta_registerAmount.append([userName, -amount, timeStemp])
            print(howMochAmount(userName))


def TRANSFER(SENDER_USERNAME, RECEIVER_USERNAME, AMOUNT, TIMESTAMP):
