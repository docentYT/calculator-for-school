database = {}

def add_user(login, password, mail):
    if database.get(login): raise ValueError("Login jest zajęty")
    new_user = {
        "password": password,
        "mail": mail
    }
    database[login] = new_user

def get_user(login):
    return database.get(login)

def update_user(login, password = None, mail = None):
    if not database.get(login): raise ValueError("Użytkownik nie istnieje")
    if password:    database[login]["password"] = password
    if mail:        database[login]["mail"]     = mail

def del_user(login):
    if database.get(login): database.pop(login)


add_user("aa", "bb", "aa@bb.pl")
print(get_user("aa"))
update_user("aa", mail="abc@cba.pl")
print(get_user("aa"))
del_user("aa")
print(get_user("aa"))