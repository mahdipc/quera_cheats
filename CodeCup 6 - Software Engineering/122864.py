ct_team = []
t_team = []

ct_team_time = []
t_team_time = []


userName_money = []
userName_health = []


def existInTeam(userName, pm=True):
    if (userName in ct_team) or (userName in t_team):
        if pm:
            print("you are already in this game")
        return True
    return False


def zarfiatTeam(isCt):

    if isCt:
        if len(ct_team) > 10:
            print("this team is full")
            return False
    else:
        if len(t_team) > 10:
            print("this team is full")
            return False
    return True


def add_user(userName, isCt, time):
    if ~existInTeam(userName):
        if zarfiatTeam(isCt):

            if isCt:
                ct_team.append(userName)
                ct_team_time.append(time)
                print("this user added to Counter-Terrorist")
            else:
                t_team.append(userName)
                t_team_time.append(time)
                print("this user added to Terrorist")


def get_money(userName, time):
    if ~existInTeam(userName, False):
        print("invalid username")
        return
    for item in userName_money:
        if (item[0] == userName) and (time == item[1]):
            print(item[2])
            return item[2]


def get_health(userName, time):
    if ~existInTeam(userName, False):
        print("invalid username")
        return
    for item in userName_health:
        if (item[0] == userName) and (time == item[1]):
            print(item[2])
            return item[2]


def Tap(attacker, attacked, types, time):
    if ~existInTeam(attacker, False):
        print("invalid username")
        return
    if ~existInTeam(attacked, False):
        print("invalid username")
        return
    if get_health(attacker, time) == 0:
        print("attacker is dead")
    if get_health(attacked, time) == 0:
        print("attacked is dead")
