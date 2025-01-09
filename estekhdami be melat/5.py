from datetime import datetime


def is_expired(session, current_time):

    t1 = datetime.strptime(session["login_time"], "%Y/%m/%d:%H:%M:%S")
    t2 = datetime.strptime(current_time, "%Y/%m/%d:%H:%M:%S")
    t = abs(int((t2 - t1).total_seconds()))

    return t >= 600


def add_log(logs, level, message, timestamp):
    log = {"level": level, "message": message, "timestamp": timestamp}
    logs.append(log)
    print(f"[{level}] {message}")


def register(users, logs, username, password, role, timestamp):
    if username in users:
        add_log(logs, "ERROR", "user already registered", timestamp)
        return

    users[username] = {
        "username": username,
        "password": password,
        "role": role,
        "balance": 0,
        "active_session": None,
    }
    add_log(logs, "INFO", "user registered successfully", timestamp)


def login(
    users,
    logs,
    username,
    password,
    timestamp,
    new_id,
):
    if username not in users or users[username]["password"] != password:
        add_log(logs, "ERROR", "invalid credentials", timestamp)
        return

    user = users[username]
    if user["active_session"]:
        add_log(logs, "INFO", "already logged in", timestamp)
        if is_expired(user["active_session"], timestamp):
            user["active_session"] = {"id": new_id[0], "login_time": timestamp}
            new_id[0] += 1
        return

    user["active_session"] = {"id": new_id[0], "login_time": timestamp}
    new_id[0] += 1
    add_log(logs, "INFO", "user logged in successfully", timestamp)


def get_session_user(users, logs, session_id, timestamp):
    for username, user in users.items():
        if user["active_session"] and user["active_session"]["id"] == session_id:
            if is_expired(user["active_session"], timestamp):
                add_log(logs, "ERROR", "session expired", timestamp)
                return
            return user

    add_log(logs, "ERROR", "session expired or invalid", timestamp)
    return


def logout(users, logs, session_id, timestamp):
    user = get_session_user(users, logs, session_id, timestamp)
    if not user:
        return

    user["active_session"] = None
    add_log(logs, "INFO", "user logged out", timestamp)


def deposit(users, logs, session_id, amount, timestamp):
    user = get_session_user(users, logs, session_id, timestamp)
    if not user:
        return

    user["balance"] += amount
    add_log(logs, "INFO", "amount deposited successfully", timestamp)


def withdraw(users, logs, session_id, amount, timestamp):
    user = get_session_user(users, logs, session_id, timestamp)
    if not user:
        return

    if user["balance"] < amount:
        add_log(logs, "ERROR", "insufficient funds", timestamp)
        return

    user["balance"] -= amount
    add_log(logs, "INFO", "amount withdrawn successfully", timestamp)


def transfer(
    users,
    logs,
    session_id,
    targot_user,
    amount,
    timestamp,
):
    user = get_session_user(users, logs, session_id, timestamp)
    if not user:
        return

    if targot_user not in users:
        add_log(logs, "ERROR", "target user not found", timestamp)
        return

    if user["balance"] < amount:
        add_log(logs, "ERROR", "insufficient funds", timestamp)
        return

    targot_user = users[targot_user]
    user["balance"] -= amount

    targot_user["balance"] += amount
    add_log(logs, "INFO", "amount transferred successfully", timestamp)


def query_logs(
    logs,
    level,
    start_time=None,
    end_time=None,
    timestamp=None,
):
    level = level.upper()
    filter = [log for log in logs if log["level"] == level]
    if start_time and end_time:
        filter = [log for log in filter if start_time <= log["timestamp"] <= end_time]

    if not filter:
        print("no logs found")
    else:
        for log in filter:
            print(f"{log['timestamp']} {log['level']} {log['message']}")

    debug_msg = f"get log {level.lower()}"
    if start_time:
        debug_msg += f" {start_time}"
    if end_time:
        debug_msg += f" {end_time}"
    add_log(logs, "DEBUG", debug_msg, timestamp)


def prosecc(users, logs, new_id, command):
    parts = command.strip().split()
    if parts[0] == "register":
        register(users, logs, parts[1], parts[2], parts[3], parts[4])
    elif parts[0] == "login":
        login(users, logs, parts[1], parts[2], parts[3], new_id)
    elif parts[0] == "logout":
        logout(users, logs, int(parts[1]), parts[2])
    elif parts[0] == "deposit":
        deposit(users, logs, int(parts[1]), float(parts[2]), parts[3])
    elif parts[0] == "withdraw":
        withdraw(users, logs, int(parts[1]), float(parts[2]), parts[3])
    elif parts[0] == "transfer":
        transfer(users, logs, int(parts[1]), parts[2], float(parts[3]), parts[4])
    elif parts[0] == "log":
        if len(parts) == 3:
            query_logs(logs, parts[1], timestamp=parts[2])
        elif len(parts) == 5:
            query_logs(logs, parts[1], parts[2], parts[3], parts[4])


users = {}
logs = []
new_id = [1]

n = int(input())
for _ in range(n):
    s = input()
    prosecc(users, logs, new_id, s)
