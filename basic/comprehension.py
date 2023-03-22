"""================ comprehensions ================"""
# Генерация последовательностей в одну строку используя цикл (синтаксический сахар)
 
# list, set, dict 
"""================ Синтаксис ================="""
# result for element in iterable_object
# result ror element in iterable_object if filter

"""================= List comprehension ================"""
# Упрощенный подход к созданию списков 

# list_ = []
# for i in range(11):
#     list_.append(i)
# print (list_)

# a = list((i for i in range(11)))
# print (a)

# list_ = [i for i in range(11)]
# print (list_)
"""================================="""
import time
# start_time = time.time()

# list_ = []
# for i in range(1000):
#     list_.append(i)
# time1= time.time() - start_time

# start_time = time.time()
# list_2 = [i for i in range(1000)]
# time2 = time.time() - start_time
# print (time1, time2)
"""================================="""
# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#         list_.append(i)
# print (list_)

# list_2 = [i for i in range(11) if i%2==0]
# print (list_2)
"""================================="""
# list_2 = [i for i in range(0,11,2)]
# print (list_2)
"""================================="""
# list_2 = [i for i in range(11) if i%2!=1]
# print (list_2)
"""================================="""
# list_3 = [i for i in ['hello']*10]
# print (list_3)
"""================================="""
# print ([input() for i in range(10)])
# Па каждой итерации запрашивает ввод(Input)
"""================================="""
# list_ = [f'{i}-Нечетное' if i % 2 else f'{i}-Четной' for i in range(100)]
# print (list_)
''' Если в условии нужен else, то все условие пишется перед for '''
"""================================="""
# Упрощенный подход к созданию списка, задействует цикл for и if-else.(ускоренная работоспособность)
# list1 = [1,'hello',3,'a',4.0,6,8,'hw']
# list2 = [f'{i}-Нечетное' if i % 2 else f'{i}-Четной' for i in list1 if type(i)==int or type(i)==float]
# print (list2)

"""================ set comprehension ================"""
# Почти тоже самое, что и представление списков. Используются фигурные скобки, не соддержит дубликатов, не гарантирует сохранность порядков элемента
# set_ = [i for i in range(11)]
# set2 = [i for i in set_]
# print (set2)
# list1 = [1,'hello',3,'a',4.0,6,8,'hw']
# set_ = {f'{i}- Четное' if i%2==0 else f'{i} Нечетное' for i in list1 if type(i)== int or type(i)==float}
# print (set_)
"""================= dict comprehension ================""" 
# Отрабатывает также, но необходимо определить ключ

# dict_ = {i:'Good' for i in range(10)}
# print (dict_)
''' Под капотом '''
# dict_ = {}
# for i in range(10):
#     dict_.update({i:'Good'})
# print (dict_)
"""================================="""
# list_ = [1,1,2,2,2,4,5,6]
# dict_ = {i:list_.count(i) for i in list_}
# print(dict_)
"""================================="""

# d = {'a': 2, 'b':3}
# c = {k:f'{v}Чет' if v%2==0 else f'{v}Нечет' for k, v in d.items()}
# print (c)
"""================================="""
# d = {i:str(i) for i in range(1,11)}
# print (d)
"""================================="""
# list1 = [1,2,9,4,5]
# list2 = ['a','b','c','d','e']
# list3 = {list1[i]: list2[i] for i in range(len(list1))}
# print (list3)

"""================ Вложенные comprehension ================="""

# dict_ = {i: list(range(1,i+1)) for i in range(1,5)}

# dict_ = {i: [j for j in range(1, i+1)] for i in range(1,6)}
# print(dict_)
"""================================="""
# dict_ = [["'hello world'"for i in range(10)]for j in range(10)]
# print (dict_)
"""================================="""
employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
    }}
# for info in employees.values():
#     # print(info)
#     for k, v in info.items():
#         print (k,v)
#         if k == 'age':
#             info[k] = float(v)

# print (employees)

# print ({id_: info for id_, info in employees.items()})
print ({id_: {k: (float(v) if k == 'age' else v) for k, v in info.items()} for id_, info in employees.items()})

