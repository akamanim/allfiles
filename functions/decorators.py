p = print
''' ================== Декораторы ================= '''
# def f():
#     print ('hello')
# print (type(f))
# a = f
# a()
''' Функция высшего порядка -> принимает как аргумент и/или возвращает функцию '''
''' Декоратор -> функция высшего порядка, позволяет обернуть другую функцию для расширения функционала( не изменяя код) '''
# def a():
#     print ("I'm a function ")

# def b(func):
#     print(f'Hello, {func.__name__}')
#     func()
# b(a)
''' ========================================== '''
''' Создаем програму которая будет считывать время, потраченное на исполнение какого-либо кода '''
def benchmark(func):
    import time 
    start = time.time()
    func()
    finish = time.time()
    print(f'Время выполнения функции {func.__name__}, заняло: {finish-start} ')

# def loop():
#     i = 0
#     range_number = 1000000
#     while i < range_number:
#         print (i)
#         i += 1
# benchmark(loop)

# def add():
#     ls = []
#     for i in range(100000):
#         ls.append(i)
#         print (i)
# benchmark(add)
''' ===================== Синтаксис декораторов ===================== '''
''' дают нам возможность изменить поведение функции, не изменяя её код. '''
# def decorator_func(func):
#     def wrapper():
#         print ('Function обертки ')
#         print ('Выполняем обертываемую функцию')
#         func() 
#         print ('Выход из обертки')
#     return wrapper
        
# # @ -> синтаксический сахар 
# @decorator_func
# def say_hi():
#     print ('hi')
# # say_hi()
# say_hi = decorator_func(say_hi)
# say_hi()


# def uppercase_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper()

# @uppercase_decorator
# def say_hi():
#     return 'hello baby'

# p(say_hi)
''' ===================== декораторы с аргументами ===================== '''
''' Универсальная запись '''
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         p('hello')
#     return wrapper

# @decorator
# def func1():
#     p('Python27')

# func1()
# def smart(func):
#     def wrapper(q,w):
#         if q == 0 or w == 0:
#             print ('Ошибка, деление на ноль!')
#             return None
#         return func(q,w)
#     return wrapper
            
# @smart           
# def division(a,b):
#     return a/b

# p(division(5,0))

# def smart(a):
#     def inner_func(func):
#         def wrapper():
#             for i in range(a):
#                 func()
#         return wrapper
#     return inner_func

# @smart(50)
# def func():
#     print ('abs')

# func()
''' ========================================== '''

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + "/<strong>"
#     return wrapper 

# def div(func):
#     def wrapper(*args,**kwargs):
#         return "<div>" + func() + "/<div>"
#     return wrapper
# @div
# @strong
# def get():
#     return "Jhon Snow"

# p(get())

''' ========================================== '''

