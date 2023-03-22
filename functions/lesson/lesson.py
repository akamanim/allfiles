'''  python3 -m venv venv '''
''' source venv/bin/activate '''
''' pip install -U pytest '''
# def add_one (x:int) -> int:
#     return x+1


# def division(x: int , y: int)-> float:
#     if y == 0:
#         raise ZeroDivisionError('Ошибка. Деление на ноль!')
#     return x/y

# def add(x: int,y:int)-> int:
#     return x + y

# def is_palindrom(string: str) -> bool:
#     if string == string[::-1]:
#         return True
#     return False

db = [
    {'name': 'Ivan', 'password':hash('121311')},
    {'name': 'Petr', 'password':hash('727375')},
    {'name': 'Leonid', 'password':hash('bob123')}
]
def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False 

print (in_database('petya'))
def register(name,password1,password2):
    if in_database(name):
        raise Exception('Данный логин занят!')
    if password1 != password2:
        raise Exception("Пароли не совпадают!")
    if len(password1) < 6:
        raise Exception('Пароль должен состоять минимум из 6 символов')
    user = {'name':name, 'password':hash(password1)}
    db.append(user)
    return 'Регистрация прошла успешно!'

# print (register('Hello','1213111','1213111'))
def login(name,password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль введен не верно!')
    return 'Авторизация прошла успешна!'

# print (login(name=input('Введите имя пользователя: '),password=input('Введите пароль: ')))
# print (register(input('Придумайте имя: '),(input('Придумайте пароль: ')),input('Подтвердите пароль: ')))

def main():
    print ('Добро пожаловать!')
    while True:
        action= input('Register: 1,Login: 2,Quite: 3. - ')
        if action == '3':
            break
        elif action == '1':
            name = input('Придумайте имя: ')
            p1 = input('Придумайте пароль: ')
            p2 = input('Подтвердите пароль: ')
            print (register(name,p1,p2))
        elif action == '2':
            name = input ('Введите логин: ')
            p1 = input('Введите пароль: ')
            print (login(name,p1))
        else:
            print('Неккоректный ввод')
main()
print (db)