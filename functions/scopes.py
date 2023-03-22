''' ====== Области видимости и пространства имен ====== '''
# Пространство имен подразделяется на 4 вида:
# 1. builtins (встроенное)
# print()
# len()
# abs()
# input()

# 2. Global (Глобальное) -> Все имена внутри файла  
# a = 89
# b = 29

# 3. Enclose -> Пространство находящееся между двумя пространствами (не всегда есть)

# 4. local (Локальная) -> внутри функции
#  print (dir(__builtins__)) -> Возвращает список встроенных классов, обьектов и функций

# print(globals()) -> Показывает все глобальные переменные 
# print (globals()['b']) -> Вызывает содержимое переменной по имени!
# print (b is globals()['b']) -> Проверяет являктся ли переменная глобальной
# globals()['y'] = 'Hello World' -> СОздает глобальную переменную
# globals()['y'] = 'Hello ' -> Меняет значение глобальной переменной
# print(y)

# def hello():
#     a = 'HoLya'
#     print (a)
#     print (locals()) -> Показывает все локальные переменные 
# hello()
# print (a) -> KeyERROR

# def func(a,b): # Параметры и аргументы тоже являются локальными!
#     x = 7
#     print (locals())
# func (3,5)

''' Enclose -> вложенность в функциях '''

# x = 'Это глобальная переменная '

# def some_func():
#     x = ' это enclose переменная '
#     def some_func2():
#         x = 'Это локальная переменная '
#         print (x)
#     some_func2()
#     print(x)
# print (x)
# some_func()

''' Порядок поиска переменной '''
# local > enclose > global > builtins 

# global -> Позволяет менять значение глобальной переменной, находясь в локальном пространстве

# a = 8 
# def func():
#     global a
#     a += 100
#     return a
# print (a) # Таким способом можно изменить глобальную переменную, с локального пространства

# a = 9

# def outer_func():
#     global a
#     a = 8

#     def inner_func():
#         global a
#         a = 8
#         print('inner', a)
#     inner_func()

#     print('outer', a)
# outer_func()
# print(a)

''' nonlocal '''

# def f1():
#     a = '1'
#     def f2():
#         def inner2():
#             nonlocal a
#             a = 2
#             print(a)
#         inner2()
#     f2()
#     print(a)
# f1()

# def counter(i):
#     count = 0
    
#     def add():
#         nonlocal count
#         print (count)
#         count += 1
#     for i in range(i+1):
#         add()
# counter(12)
























