import json

register = {}
with open ('reg.json', 'w') as file:
    json.dump(register,file)

log = int(input('Введите логин: '))
password = int (input('Введите пароль:'))
def regist (log, password):
    with open('reg.json', 'r') as file:
        reg = json.load(file)
    if log not in reg:
        reg[log] = password
        with open ("reg.json", "w") as file:
            json.dump(reg,file)
        print ('регистрация прошла успешно')
    else:
        print('Такой логин уже существует')