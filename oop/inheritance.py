''' ==================== Основные принципы ООП, Наследование =================== '''

'''
Наследование
Инкапсуляция 
Полиморфизм
Абстракция
Ассоциация (Агрегация, Композиция)
'''

''' Наследование - принцип ООП, в котором мы можеж унаследовать, переопределить и использовать в дочернем классе все атрибуты и методы родительского класса. '''

class Человек:
    def get_hot(self):
        print('Я умею ходить!')
    def get_dis(self):
        print('Я могу кушать!')

class Работа:
    def get_money(self):
        print ('Я зарабатываю деньги!')

class Доктор(Человек,Работа):
    def get_doc(self):
        print ('Я могу лечить людей!')

class Кузнец(Человек,Работа):
    def get_kuz(self):
        print('Я могу из любого металла, сделать изделие!')

class Хирург(Доктор):
    def get_work(self):
        print ("Я могу резать людей!")

class Подмастерия(Кузнец):
    def get_help(self):
        print ('Я могу помочь кузнецу с его работой!')

доктор = Хирург()
Ученик_Кузнеца = Подмастерия()
                                                                                                                                  
Ученик_Кузнеца.get_kuz()
Ученик_Кузнеца.get_help()
Ученик_Кузнеца.get_dis()
# print(Подмастерия.__mro__) # Порядок поиска атрибутов
print ('')


''' ==================== Виды наследования =================== '''
# 1. Одиночное наследование (в дочернем классе наследуемся от одного класса)
# 2. Иерархическое наследование (Когда от одного родителя много дочерних классов)
# 3. Многоуровневое наследование (Несколько поколений)
# 4. Множественное наследование (Когда перечисляем родителей через запятую)
# 5. Гибридное наследование (более двух предыдущих пунктов)

''' =========================================================== '''

class Person:
    def __init__(self,name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name
    def display_info(self):
        print(f' Name: {self.name}')
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}, {self.age} лет'
class Employee(Person):
    def work(self):
        print (f'{self.name} Работает')

class Student(Person):
    # def __init__(self,name, age, last_name,class_):
    #     self.class_ = class_
    #     self.name = name
    #     self.age = age                                       # Один из вариантов
    #     self.last_name = last_name

    # def __init__(self,name,age,last_name,class_):            # Второй вариант
    #     Person.__init__(self,name,age,last_name)
    #     self.class_ = class_

    def __init__(self, name, age, last_name,class_):           # Третий вариант
        super().__init__(name, age, last_name)
        self.class_=class_

    def study(self):
        print(f'{self.name} учится')

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}.{self.age} лет.Ученик {self.class_}-го класса.'
    

st1 = Student('Митхат',14,'Ахметов',7)
tom = Employee('Том', 28,'Харди')
print (st1)
print (tom)
tom.work()
st1.study()

''' =========================================================== '''

# isinstance -> проверяет является ли обьект экземпляром класса.
print (isinstance(st1, Employee)) # False
print (isinstance(st1, Person)) # True
# issubclass -> Проверяет является ли класс подклассом другого класса
# print(issubclass(Подкласс, Родитель))
print (issubclass(Employee,Person)) # True

''' =========================================================== '''
print ('\n'*20)
''' ================== Множественное наследование ================= '''

class Lion:
    color = 'Black'

class Lioness:
    color = 'Brown'

class Simba(Lion, Lioness):
    pass

obj = Simba()
print (obj.color)

''' =========================================================== '''

class Grandpa:
    def sleep(self):
        print ('Дедушка спит!')

class Grandma:
    def cook(self):
        print ('Бабушка готовит!')

class Father:
    last_name = 'Mr Smit'
    def work(self):
        print ('Папа на работе!')

class Mother(Grandpa,Grandma):
    last_name = 'Ms Smit'

class Child (Father,Mother):
    pass
child = Child()
child.work()
child.cook()
child.sleep()
print(child.last_name)

''' ======== Проблемы множественного наследования ======== '''
# 1 -> Проблема Ромба (mro)
# class A:
#     pass                                  #         A
# class B(A):                               #      /     \
#     pass                                  #     B       C
# class C(A):                               #      \     /
#     pass                                  #         D
# class D(B,C):
#     pass
# 2 -> Проблема скрещенного наследования
# class X:
#     pass
# class Y:
#     pass
# class A(X,Y):
#     pass
# class B(Y,X):
#     pass
# class M(B,A):
#     pass

'''
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    def describe_user(self):
        print (f'Имя: {self.first_name},\n Фамилия {self.last_name}.\n Возраст: {self.age}.\n Город: {self.city}')
    def greet_user(self):
        print (f'Здравствуйте {self.first_name}!')
    def __str__(self) -> str:
        return f'Здравствуйте {self.first_name}!'
class Admin(User):
    def __init__(self, first_name, last_name, age, city) :
        super().__init__(first_name, last_name, age, city)
        self.privileges = []
    def set_privileges(self,p):
        self.privileges.append(p)
    def show_privileges(self):
        print (f'{self.privileges} - Ваши привилегии!')

first_name = input("Введите имя: " )
last_name = input("Введите фамилию: ")
try:
    age = int(input("Ваш возраст: "))
except:
    print('Вы ввели неверный возраст, введите цифру!')
    age = int(input("Ваш возраст: "))
city = input("Введите город: ")
# privileges = list(input("Привилегии которыми вы обладаете: "))
user1 = User(first_name, last_name,age,city)
admin = Admin(first_name, last_name, age, city)
admin.set_privileges('Удалить пользователя')
admin.show_privileges()
user1.describe_user()
'''
'''~~~~~~~~~~ Миксины ~~~~~~~~~~~'''
# Классы для наследования. От них не создаются обьекты
# class MoveMixin:
#     def move(self):
#         print('Движение')
# class StopMixin:
#     def stop(self):
#         print('Стою')
# class Person(MoveMixin,StopMixin):
#     pass
# class Car(MoveMixin,StopMixin):
#     pass
''' =========================================================== '''
class PersonInitMixin:
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

class PersonIntoMixin:
    def get_info(self):
        print(f'Имя: {self.name} {self.last_name}, Возраст: {self.age}')

class Person(PersonInitMixin, PersonIntoMixin):
    pass

Man = Person('Mitya','Ahmetov',25)
Man.get_info()

class Student(PersonInitMixin,PersonIntoMixin):
    def __init__(self, name, last_name, age, course):
        super().__init__(name, last_name, age)
        self.course = course
    def get_info(self):       
        return super().get_info(),print (f'Студент {self.course}-го курса ')

st = Student('Mitya', 'Ahmetov',22,4)
st.get_info()
# 1. Имена заканчиваются на Mixin
# 2. Не предназначен для создания обьектов
# 3. Нужны для расширения функционала др класса
''' =========================================================== '''
''' Создать класс Note с атрибутом класса todo = {}, createMixin, UpdateMixin, DeleteMixin, ReadMixin'''
print ('\n' * 5)
class CreateMixin:
    def createmix(self):
        try:    
            a = input('В каком формате вы хотите установить новый ключ? - (Числовой/Строчный)')
            if a.lower() == 'числовой':
                b = int(input("Введите ключ - "))
                for k,v in self.todo.items():
                    if b == k:
                        raise ValueError
                c = input('Введите содержимое ключа - ')
                dict_ = {b:c}
                self.todo.update(dict_)
                print(self.todo)
            elif a.lower() == 'строчный':
                b = input("Введите ключ - ")
                for k,v in self.todo.items():
                    if b == k:
                        raise ValueError
                c = input('Введите содержимое ключа - ')
                dict_ = {b:c}
                self.todo.update(dict_)
                print(self.todo)
            else:
                print('Некоректный тип ключа')    
        except ValueError:
            print('Такой ключ уже существует!')
        
class UpdateMixin:
    def updatemix(self):
        try:
            type_key = input("Введите тип ключа, чтобы его изменить - (Числовой/Строчный) ")
            if type_key.lower() == 'числовой':
                a = int(input('Введите ключ, значение которого хотите изменить - '))
                for k,v in self.todo.items():
                    if k == a:
                        self.todo[a] = input('Введите новое значение - ')
                        print (self.todo)
                        break
                else:  
                    raise ValueError
            elif type_key.lower() == 'строчный':
                a = input('Введите ключ, значение которого хотите изменить - ')
                for k,v in self.todo.items():
                    if k == a:
                        self.todo[a] = input('Введите новое значение - ')
                        print (self.todo)
                        break
                else:  
                    raise ValueError
            else:
                print('Некоректный тип ключа')
        except ValueError:
            print('Такого ключа нет!')
class DeleteMixin:
    def delmix(self):
        try:
            type_key = input("Введите тип ключа, чтобы его удалить - (Числовой/Строчный) ")
            if type_key.lower() == 'числовой':
                a = int(input('Введите ключ, который хотите удалить - '))
                self.todo.pop(a)
                print(self.todo)
            elif type_key.lower() == 'строчный':
                a = input('Введите ключ, который хотите удалить - ')
                self.todo.pop(a)
                print (self.todo)
            else:
                print('Не верный тип ключа')
        except:
            print('Такого ключа нет')
class ReadMixin:   
    def readmix(self):
        for k,v in self.todo.items():
            print (f'Ключ - {k}. Значение - {v}')
        a = input('Желаете захешировать ваши ключи? (y/n) ' )
        if a == "y":
            self.todo = {hash(str(k)):v for k,v in self.todo.items()}
            print (self.todo)
        elif a == 'n': 
            print('Досвидание')
        else:
            print('Не верная команда')
class Note(CreateMixin,UpdateMixin, DeleteMixin,ReadMixin):
    todo = {}
book = Note()
book.todo = {    
    "имя": "Анна",
    "возраст": 27,
    "рост": 1.65,
    "гражданство": "Россия",
    "логин": "user123",
    "пароль": "p@$$w0rd",
    19857: 'На счету',
    25112: 'Код от телефона',
    "дата регистрации": "2022-02-14",
    }
print(book.todo.pop('несуществующий ключ', "Такого ключа нет"))
print(book.todo)
# book.createmix()
# book.createmix()
# book.updatemix()
# book.delmix()
# book.readmix()
