''' ==========  ~~~~~~~~~~~~~~~~~ ВВедение в ООП ~~~~~~~~~~~~~~~~~~  ========== '''
# ООП(Объектно ориентированное программирование) -> парадигма(набор правил) программирование. Основывается на двух ключевых понятиях -> class(Класс) и Object(Обьект)
''' ==========  ~~~~~~~~~~~~~~~~~ Классы ~~~~~~~~~~~~~~~~~~  ========== '''
#  Класс -> Предтставляет из себя какую-то схему или чертеж, или просто описания, того какими свойствами, каким поведением будет обладать обьект
''' ==========  ~~~~~~~~~~~~~~~~~ Обьект ~~~~~~~~~~~~~~~~~~  ========== '''
# Обьект -> Это экземпляр от класса, при этом у каждого обьекта, какое-то собственное  поведение и свойства и так далее
''' ==========  ~~~~~~~~~~~~~~~~~ Свойства ~~~~~~~~~~~~~~~~~~  ========== '''
# Свойства -> Обычные переменные (name = 'Tima')
# Поведение -> Это обычная функция(их также называют Методами)

''' ==========~~~~~~~~~~~~~~~~~ Синтаксис создания класса ~~~~~~~~~~~~~~~~~~========== '''
# class A:
#     string = 'атрибут класса'
    
#     def first_method(self): # Создание метода| self -> Ссылка на обьект(или по другому на экземпляр класса)
#         pass

# first_obj = A()
# second_obj = A()
# f = A()

# second_obj.first_method()
''' ==========~~~~~~~~~~~~~~~~~ Пример ~~~~~~~~~~~~~~~~~~========== '''
# class Person:
#     arms = 2
#     legs = 2
    
#     def __init__(self,name, age):
#         ''' Функция, вызывается, при создании обьекта, внутри этой функции определяются атрибуты обьекта, отвечает за инициализацию '''
#         # Атрибуты объекта (экзепляра класса)
#         self.name = name # мы добавляем в обьект self новый атрибут name  
#         self.age = age #

#     def add_one(self):
#         ''' Функция которая принимает обьект, и изменяет возраст на 1 '''
#         self.age  += 1
#     def __str__(self) -> str:
#         return f'{self.name} - {self.age} - {self.arms}'
# Person1 = Person('Mithat', 12)
# print (Person1)
''' ==========~~~~~~~~~~~~~~~~~ Экземпляр класса ~~~~~~~~~~~~~~~~~~========== '''
# Переменная класса -> (class variable) Та переменная которая находится внутри класса (Это те поля которые относятся ко всем классам)
# Переменная экземпляра класса -> (instance variable)  Внутри метода __init__ и относятся к обьекту
''' ==========~~~~~~~~~~~~~~~~~ Атрибуты класса ~~~~~~~~~~~~~~~~~~========== '''
# Переменные внутри класса (Атрибуты на уровне класса) являются статическими(т.е. константами)
# Но в дальнейшем мы можем присваивать им какие-то другие значения в ввиде исключения
# Можно обращаться через класс, не создавая какой-либо обьект
''' ==========~~~~~~~~~~~~~~~~~ Методы класса ~~~~~~~~~~~~~~~~~~========== '''
# Функции которые прописаны внутри класса
''' ==========~~~~~~~~~~~~~~~~~ Обьект класса ~~~~~~~~~~~~~~~~~~========== '''
# Обьект, экземпляр, instance класса -> Объект созданный по шаблону класса (перенимает все атрибуты и методы у класса )
''' ==========~~~~~~~~~~~~~~~~~ Атрибуты и методы обьекта ~~~~~~~~~~~~~~~~~~========== '''
# атрибуты и методы, которые есть у обьекта, но их может не быть у класса

# a = Person('One', 1)
# name, age, legs, arms
# a.a = 10
''' Класс имеет доступ только к атрибутам класса '''
''' Обьект имеет доступ к атрибутам класса и обьекта'''
''' ==========~~~~~~~~~~~~~~~~~ Класс налога ~~~~~~~~~~~~~~~~~~========== '''
class Salary:
    nalog = 15 # Процентов

    def __init__(self, zp, staj):
        self.zp = zp
        self.staj = staj
    
    def sum_nalog(self):
        summa = (self.zp * (self.staj) * 12 * self.nalog) / 100
        # print (summa) 
        return summa
    def sum_zp(self):
        s1 = self.zp * self.staj * 12 
        # print (s1)
        return s1
    
Mithat = Salary(9000, 10)
a = Mithat.sum_nalog()
b = Mithat.sum_zp()
print (f'Заработано за год было - {b} сом, {int(b/84)} в долларах США . Потрачено на налоги государству - {b-a}')
print('')

class Car:
    wheels = 4

    def __init__(self, auto_owner, model, year):
        self.owner = auto_owner
        self.model = model
        self.year = year
        self.mileag = 0

    def go(self, km):
        self.mileag += km
        return self.mileag
    def __str__(self):
        return f'Владелец - {self.owner}. Модель авто - {self.model}. Год-выпуска {self.year}, Пробег авто - {self.mileag}'

BMW = Car('Mithat', 'M5F90' , '2019')
BMW.go(25000)
print (BMW)
print ('')
# get_total() , add_total(), sub_total()
class SelfBank:
    total = 0
    def get_total(self):
        return f'Ваш баланс на данный момент - {self.total}'
    def add_total(self, skolko):
        self.total += skolko
        return f'Ваш баланс пополнен на {skolko} сом! Теперь ваш баланс {self.total}'
    def sub_total(self, subtot):
        self.total -= subtot
        return f'С вашего баланса сняли {subtot} сом! Остаток на балансе {self.total}'
    def __str__(self):
        return f'На вашем балансе {self.total} сом'
    
mitya = SelfBank()
print(mitya.get_total())
print(mitya.add_total(150000))
print(mitya.sub_total(20000))
print(mitya)
print ('')


class Student:
    knowledge = 0
    languages = {}
    books = []
    def __init__(self, name , last_name):
        self.name = name
        self.last_name = last_name 
    def read_books(self, book):
        self.books.append(book)
        print (f'За прочитанную вами книгу - {book}, вы получаете 5 баллов!')
        self.knowledge+= 5
    def do_homework(self, homework):
        self.knowledge += 10
        print (f'За сделанное вами задание - {homework}. Вы получаете 10 баллов!')
    def add_points(self, balls):
        self.knowledge = balls
        print (f'Количество ваших балов - {self.knowledge}')
    def new_language(self, new, percent):
        try:    
            
            if percent < 0 or percent > 100:
                raise ValueError
            else:
                self.languages.setdefault(f'{new}',f'{int(percent)}%')
        except:
            print  ('Вы ввели неверный формат процентов')
    def __str__(self) -> str:
        return f'Имя студента - {self.name} {self.last_name}, Владения языками - {self.languages}, Прочитанные книги - {self.books}. Количество баллов - {self.knowledge}'
    
mitya = Student('Mithat','Ahmetov')
mitya.add_points(50)
mitya.do_homework('Ключ-карта')
mitya.new_language('Python', 50)
mitya.new_language('FrontEnd', 70)
mitya.read_books('Гарри Поттер')
mitya.read_books('Самый богатый человек в Вавилоне')
print(mitya)
mitya.new_language('Python', 150)
mitya.new_language('Python', 'bla bla bla')