p = print
# # a = str(-2)
# # print (a)
# # a = pow(2,5,16)
# # print (a)

# # name_of_list = ['1234567'] 
# # new_list = name_of_list[0] 
# # i = len(new_list) 
# # if i%2==0: 
# #     new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2] 
# # else: 
# #     new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1] 
# # print(list(new_list))

# # list_ = ['world', 'hello']
# # new_list = [list_[1]]
# # new_list.append(list_[0])
# # print (new_list)

# # suitcase = []
# # suitcase.append('Футболка')
# # suitcase.append('Шорты')
# # suitcase.append('Сланцы')
# # suitcase.append('Кепка')
# # suitcase.append('Очки')
# # del suitcase[-1]
# # suitcase.insert(0,'Панама')
# # print (suitcase)

# # # a = input()
# # list_ = []
# # tuple_ = (' ',)
# # for i in a:
# #     if i > '0':
# #         list_.append(i)
# #         tuple_= i,
# # print (list_,tuple_)

# # a = input().split(",")

# # list_ = [1, 2, 3, 4, 5] 
# # new_list = [] 
# # for x in list_: 
# #     if x % 2 == 0:
# #          x = 'четное' 
# #          new_list.append(x) 
# #     elif x % 2 != 0:
# #          x = 'нечетное' 
# #          new_list.append(x) 
# # print(new_list)

# # name = input('Введите имена через пробел: ').lower().split()
# # guests = input('Введите имя: ').lower().split()
# # for guest in guests:
# #     if guest in name:
# #         print (f'welcome - {guest}')
# #     else:
# #         print (f'good bye - {guest}')

# # list_ = []
# # for i in range(0,100):
# #     if i % 2 == 0:
# #         list_.append(i)
# # print (list_)

# L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# L = [t for t in L if t]
# print(L)

# # list_ = [] 
# # name1 = input("Введите имя и фамилию: ") 
# # name2 = input("Введите имя и фамилию: ") 
# # name3 = input("Введите имя и фамилию: ") 
# # name4 = input("Введите имя и фамилию: ") 
# # name5 = input("Введите имя и фамилию: ") 
# # list_.append(name1) 
# # list_.append(name2) 
# # list_.append(name3) 
# # list_.append(name4) 
# # list_.append(name5) 
# # target = " " 
# # surnames = [] 
# # for x in list_:
# #      t = x.find(target) 
# #      v = x.rfind(target) 
# #      if x.count(target) > 1: 
# #          surnames.append(x[v+1:]) 
# #      else: 
# #          surnames.append(x[t+1:]) 
# # print(sorted(surnames))

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# sum_ = 0 
# for i in str(list_):
#     if i.isdigit():
#          sum_ = sum_ + int(i)
#          print (sum_)
# print (sum_)
# # lists = [ [13],[13]] 
# # max_ = max([x for x in lists], key=len) 
# # min_ = None 
# # if len(lists) > 1: 
# #     min_ = min([x for x in lists],key=len) 
# #     if max_ == min_: 
# #         min_ = None 
# # print(f'max_list {max_}') 
# # print(f'min_list {min_}')
# a = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
# # b = ('a')
# # c = []
# # for i in a:
# #     if i.lower()[0] in b:
# #         c.append(i)
# # print(c)

# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1, 2]]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
            
#             break
#         elif i != j:
#             c.append(i)
# print(c)

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]


# diff = list(set(colors1) - set(colors2))
# between = list(set(colors1) & set(colors2))
 
# print(diff,between)    

# colors1 = ["red", "orange", "green", "blue", "white"] 
# colors2 = ["black", "yellow", "green", "blue"] 
# resc1=[] 
# resc2=[] 
# for i in colors1: 
#     if not i in colors2: 
#         resc1.append(i) 
# for k in colors2: 
#      if not k in colors1: 
#         resc2.append(k) 
# print(resc1,resc2)

# list1 = [1,2,3,4,5] 
# list2 = [5,6,7,8,9] 
# res = None 
# for i in list1: 
#     for j in list2: 
#         if i==j: 
#             res = True 
#             break 
#         else: res = False 
# print(res)


# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8] 
# repeats = 3 
# res = [] 
# for i in list_: 
#     if list_.count(i) >= repeats and i not in res: res.append(i) 
# print(res)

# from itertools import permutations 
# list_ = [1, 2, 3] 
# comb = permutations(list_) 
# for i in comb: print(i)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"] 
# res = [] 
# for x in colors: res.append(x[::-1]) 
# print(sorted(res, key=len))

# list_ = [1,2,3,4,5,6,7,8,9,0] 
# step = 2 
# element = 'A' 
# i = step 
# while i < len(list_) + 1: list_.insert(i, element) 
# i += step + 1 
# print(list_)

# a = {'x': 1, 'y': 2, 'z': 1}
# print (a['x'])

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k,v in a.items():
#     if v% 2 == 0:
#         b.setdefault(k,2)
#     else:
#         b.setdefault(k,v)
# print (b)


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for k,v in a.items():
#     if v == None:
#         b.pop(k,v)
#     else:
#         b.setdefault(k,v)
# print (b)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# b = {}
# for k,v in a.items():
#     if 5>2:
#         b.setdefault(k, v/5)
# print (b)

# a = {'a': 3, 'b': 2}
# b = 0
# for k,v in a.items():
#     b = b + v
#     print (b)
# print (b)

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for k,v in dict_.items():
#     if v != None:
#         b.pop(k,v)
#     else:
#         b.setdefault(k,v)
# print (b)

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k,v in dict1.items():
#     if 5>1:
#         dict2.setdefault(k**2,v)
# print (dict2)

# # list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# # dict_ = {}
# # for k in list_:
# #     dict_.setdefault(k,len(k))
# # print (dict_)

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# dict2 = {}
# for k,v in dict_.items():
#     if 5>1:
#         dict2.setdefault(len(k))
# print (max(dict2))


# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k,v in list(dict_.items()):
#     for v2 in v.values():
#         dict_[k] == v2
# print (dict_)
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k,v in list(dict1.items()):
#     for v2 in v.values:
#         dict2.setdefault(k,v2*v2)
# print (dict2)

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}} 
# dict2 = {} 
# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): res = res * j 
#     dict2[k] = res 
# print(dict2)

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding'] 
# ls = [x for x in list_ if type(x)==int] 
# ls2 = [x for x in list_ if type(x)==str] 
# dict_ = dict(zip(ls2, ls)) 
# print(dict_)

# tilek = {'Dodo','ImperiaPizza','FreshBox'} 
# timur = {'OchakKebab','FreshBox'} 
# alexander = {'FreshBox', 'KFC'} 
# elina = {'Dodo','ImperiaPizza','FreshBox','OchakKebab','KFC'} 
# restoran = tilek.intersection(timur).intersection(alexander).intersection(elina)
# print (restoran)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard("колбаса")
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.remove("cыр чеддар")
# ingredients.add("сыр моцарелла")
# print (ingredients)


# a =[set(), set(), set()]
# inp1 = input('Введите данные через пробел ').split()
# inp2 = int(input('В какое множество записать? (1-3) '))
# for i in range(len(a)):
#     if inp2 == i + 1:
#         a[i].update(set(inp1))
#     else:
#         a[i].add('default value')
# print(a)

# list_ ["True" if i%2==0 else "False" for i in range(1,10)]
# print (list_)

# dict_ = {i:i**2 for i in range(1,11)}
# print (dict_)

# n = int(input())
# dict_ = {i:i**2 for i in range(1,501) if i%n==0}
# print (dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k:[i for i in range(1,j)]for k,j in a}
# print (dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# dict_ = {k:list(range(v+1))[1:] for k,v in a.items()} 
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k:('odd' if v%2==0 else 'even') for k,v in dict_.items()}
# print (a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending' 
# list1 = list(string_.split())
# list_ = [i for i in list1 if i.isdigit() ]
# print (list_)

# list_ = {k:v for k,v in range(1,26,1)}
# print (list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} 
# list1 = [y for k,v in dict_.items() for x,y in v.items()]
# print(list1)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_ = {i:len(i)**2 for i in list_name if len(i)}
# print (dict_)

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110} 
# list1 = [k.upper() for k,v in dict_.items() if 200 < v < 5000] 
# print(list1)

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try: 
#     print (dict_.get('key1','asd'))
# except KeyError:
#     print ('Нет такого ключа!')

# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError
# except Exception as e:
#     print (f'{e.__class__}Введён некорректный возраст')
# except ZeroDivisionError:
#     print ('Доступ запрещен')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# # list_.add(range(0,10))

# try:
#     list_.append(range(0,10))
# except NameError:
#     print ('Че нах')
# print (list_)
# list_ = [1, 2, 3, 4]
# for i in range(0, len(list_) + 1):
#     print(list_[i])


# password = 'shoasdasdrt'
# try:
#     if len(password) < 6:
#         raise ValueError()
# except ValueError:
#     print ('fafa')

# def to_fahrenheit(k:int) -> float: 
#     assert k>=0,'Холоднее абсолютного нуля!' 
#     res=(k-273.15)*9/5+32 
#     return res 
# print(to_fahrenheit(3))

# def filter_comment(comment='', banlist=[]) :
#     try:
#         for x in comment.lower().split():
#             print (x)
#             if x.lower() == str(banlist).lower():
#                 raise ValueError
                
#         else:
#             print (comment)
#     except ValueError:
#         print ('Ваш комментарий отправлен на перепроверку,так как, возможно, содержит неблагоприятный контекст')
# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!',['bob','really'])

# def collect_all_possibles(list_: list, num: int) -> list: 
#     result=[] 
#     for x in list_: 
#         try: 
#             result.append(x*num) 
#             result.append(x+num) 
#             result.append(x-num) 
#             result.append(x**num) 
#             result.append(x//num) 
#             print (result)
#         except TypeError: 
#             continue 
#             return result
# collect_all_possibles([1,2,3],5)

# def get_type(a,b):
#     print(type(a))
#     print(type(b))
# get_type(12,'asda')

# dict_={}
# def dictionary(dict_):
#     for element in dict_:
#         print (element)

# num = 3
# def check(num):
#     if num%2==0:
#         print ('It is odd number')
#     else:
#         print ('It is even number')
# check(num)

# def is_palindrome(a):
#     if a == a[::-1]:
#         return ('True')
#     else:
#         return ('False')
# print (is_palindrome('mom'))

# def multiply_list(list_):
#     a = 1
#     for i in list_:
#         a*=i 
#         return a
# print(multiply_list([1,2,3,4,5,6]))

# def multiply_list(list_): 
#     n = 1 
#     for i in list_: 
#         n *= i
#     return n   
# print(multiply_list([1, 2, 3, 4, 5, 6]))

# def sum_digits(a):
#     n = 0
#     for i in str(a):
#         print (i)
#         n = n + int(i)
#     return n
# print (sum_digits(111))

# def func11(a,b,c):
#     if c!=0:
#         return ((a+b)/c)
#     else:
#         return (a+b)
# print(func11(4,7,0))


''' Создайте функцию-менеджер calc, которая будет принимать в себя два числа и операцию.
Должны быть доступны операции(+, -, /, *).
Создайте также 4 доп.функции - add_, sub_, div_, mult_, которые будут принимать в себя два числа.
Затем в зависимости от операции calc будет вызывать одну из доп.функций.
Соответственно, если операция '+', то вызывается функция add_ и т.д.'''
# def add_(a,b):
#     return a+b
# def sub_ (a,b):
#     return a-b 
# def div_(a,b):
#     return a/b
# def mult_(a,b):
#     return a*b
# def calc(num1,num2,operation):
#     if operation == "+":
#         return add_(num1,num2)
#     elif operation == "-":
#         return sub_(num1,num2)
#     elif operation == "/":
#         return div_(num1,num2)
#     elif operation == "*":
#         return mult_(num1,num2)
#     else:
#         print ('Неправильное число!')

''' Создайте функцию func15, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники ("name, скидки в магазине компьютерной техники!"), отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере '''
users = [
  { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
  { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
  { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
  { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
  { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
]
# def func15():
#     for user in users:
#         for k,v in user.items():
#             if k == 'work' and str(v.) == 'IT':


# func15()

# users = [ { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'}, { 'name': 'Helen', 'age': 35, 'work': 'Nurse'}, { 'name': 'Bob', 'age': 35, 'work': 'Driver'}, { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'}, { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'} ] 
# def func15(users):
#      r=[] 
#      for i in users: 
#         if i['work'].startswith('IT'): 
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!") 
#             r=''.join(i for i in r) 
#         return r
# print(func15(users))

# list_ = [{'name': 'Jack', 'salary': 10000, 'overTime': 4}]
# def sal():
#     for i in list_.items():
#         if list_['overTime'] > 0:
#             (list_['overTime']*200) + list_['salary']


# def foo():
#     global var
#     var = 'переменная foo'
  
#     def bar():
#       var = 'переменная bar'
#       print ('переменная в foo: ', var)
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount


# def pay_bills(amount, log_name):
#   global balance
#   balance = balance - amount
#   print (f'Вы заплатили {amount} сом за {log_name}')



# def get_balance():
#     print (f'У вас на счету {balance} сом')
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control(name):
#   for k,v in name.items():
#     if v >= 17:
#       print (f'{k} Вы можете войти в клуб')
#     else:
#       print (f'{k} извините, Вы не проходите по age-control')
#   return

# age_control(a)

# def count_symbols(name):
#   g = 0
#   s = 0
#   ost = 0
#   for element in name:
#     if element.lower() in 'яиюэёоаыуе':
#       g += 1
#     elif element.upper() in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
#       s += 1
#     else:
#       ost += 1
#   return (f'Количество гласных: {g}, согласных: {s}, остальных символов: {ost}')

# print(count_symbols('Мурат супер!'))

# def count_symbols(words): 
#   glasnue = 0 
#   soglasnue = 0 
#   symbol = 0 
#   for i in words: 
#     if i.isalpha(): 
#       if i.lower() in 'яиюэёоаыуе': 
#         glasnue += 1 
#       else: soglasnue += 1 
#     else: symbol += 1 
#   return (f'Количество гласных: {glasnue}, согласных: {soglasnue}, остальных символов: {symbol}') 
  
# print(count_symbols('Мурат супер!'))

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7(bob):
#   b =[]
#   for i in bob:
#     if i < 7:
#       b.append(i)
#   return b
# print(lower_7(a))
  

# list_ = ['123hello@gmail.com', '123', 'hello']
# res = list(map(lambda num:num if num.endswith('@gmail.com') else 'Now valid email', list_))
# print (res)

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list1 = list(filter(lambda num:num > 0 ,list_))
# list2 = list(filter(lambda num:num < 0 ,list_))
# res = list(zip(list1,list2))
# print (res)

# from functools import reduce 
# list_ = ['a', 'n', 'n', 'a'] 
# res = reduce( lambda x, y: x + y, list_) 
# if res == res[::-1]: 
#   print('YES') 
# else:  
#   print('NO')

# S = [x**2 for x in range(10)]
# print (S)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
p(factorial(5))