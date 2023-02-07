import json
register = {}
with open ('reg.json', 'w') as f:
    json.dump(register,f)
log = str (input("введите логин:"))
password = str (input("введите пароль:"))

def regist (log, password):
    with open('reg.json', 'r') as f:
        register = json.load(f)
    if log not in register.keys():
        register[log] = password
        with open ("reg.json", "w") as f:
            с
        print ('регистрация прошла успешно')
    else:
        print ('аккаунт с таким логином уже существует')