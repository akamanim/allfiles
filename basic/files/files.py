'''  ========== Файлы. Работа с файлами ========= '''
# open(путь до файла/название файла, режим) -> функция, которая позволяет отккрывать файлы 
# и работать с ними
# file = open('/home/test/desktop/test.py') -> абсолютный путь
# file = open('test.py') -> относительный путь 
''' Режимы '''
# 1. r(read) -> открывает режим для чтения.Указатель ставится в самое начало. Также если мы не указываем режим, тогда это автомотически режим для чтения(т.е по дефолту). Если вы будете считать файл, которого нет, то возникнет ошибка

# file = open('test.py')
# file = open('tasks.py', 'r')

# 2. w(write) -> Открывает файл для записи. Если вы при помощи этого режима, в котором уже записана какая-то информация, то она стирается, т.е. обнуляется, если такого файла нет, то создается новый файл.

# file = open('test.py', 'w')

# 3. a(append) -> Открывает файл добавления.Указатель будет находится в конце, если файла нет, то он создаст новый файл
# file = open ('test.py', 'a')

# 4. x(ecllusive) -> Используется нами, что бы создавать уникальные файлы, т.е. если мы попытаемся создать файл, который уже есть, возникнет ошибка

# 5. t(text) -> Открывает файл в текстовом виде. Режим по умолчанию в текстовом виде

# 6. b(binary) -> Открывает файл в бинарном виде.
# rb -> чтение в бинарном виде
#  wb -> запись в бинарном виде
#  ab -> Дозапись в бинарном виде

# 7. + -> Открывает файл как в режиме чтения, так и в режима записи
# r+
# w+


''' методы режима r '''
#  1. read() -> Если параметр не указан, то чтение до конца файла
#  2. readline() -> считывает только одну строку за раз -> str
#  3. readlines() ->считывает все строки файла -> list

# #  read
# file = open('test.py')
# data = file.readline()
# # print (data)
# print(file.tell()) # Возвращает индекс где находится наш указатель
# file.close() # файл обязательно нужно закрывать 

# file.seek(int) -> перемещает указать на указанный int 

# readline 
# file = open('test.py','r')
# data = file.readline()
# data2 = file.readline()
# print(data, data2)
# file.close()

# f = open('test.py')
# for line in f:
#     print(line)
# f.close()

# f = open('test.py')
# print(f.readlines())
# f.close()

''' Методы режима w '''
# write('string') -> Принимает в себя строку
#  wtirelines('list') -> Принимает в себя лист и будет записывать построчно 

# f = open('test2.py', 'w')
# f.write('Hello Hoja')
# f.writelines([' 1',' 2',' 3'])
# f.close()

''' Контекстный менеджер - открывает файл при любом раскладе и будет закрывать его'''

# with open('test2.py') as f:
#     print (f.read())

# # r+ 
# with open('test.py', 'r+') as file:
#     file.write('Good Morning suk r+ \n')
#     file.seek(0)
#     print(file.read())
# #  w+
# with open('test.py', 'w+') as file:
#     file.write('Good Morning suk w+ \n')
#     file.seek(0)
#     print(file.read())
# x+ -> Создает файл с уникальным названием 
# with open('test3.py', 'x+') as f:
#     f.write('Good Morning suk\n')
#     f.seek(0)
#     print(f.read())
# a+
# with open('test.py', 'a+') as file:
#     file.write('Good Morning suk\n')
#     file.seek(0)
#     print(file.read())

'''=========== JSON ==========='''
''' JavaScript Object Notation -> Единый такстовоый формат передачи и хранения данных между приложения, языками программирования frontend - backend '''

{
    "id": 1,
    "author": "John",
    # "post": null
}
''' Разница  типов данных '''
# Python                   JSON
# dict                       object
# list                       Array
# tuple                      Array
# str                        String
# int 
# float                      Number
# True                       true
# False                      false
# None                       Null

import json 
# Сериализация (Запись данных в JSON) -> перевод Python обьета в JSON 

# dump -> метод записывает Python обьект в JSON файл или файл в формате JSON 
# dumps -> метод считывает Python обьект и переводит в строку в формате JSON

# Десириализация (чтения данных из JSON) -> перевод JSON в Python обьект

# load -> считывает файлы в формате JSON и переводит в формат Python
# loads -> Считывает текст в формате JSON и переводит в формат Python


# json.loads(json_object)

# person = '{"name":"Jonh", "age":25}'
# result = json.loads(person)
# print (result)

# json.load(file) 

# with open('test.json', 'w+') as file:
#     person = '{"name":"Jonh", "age":25}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print (data.get('name'))



# json.dumps(python_object)

# person = {'name':'Jonh', 'age':25, 'hane_car':False}
# print(json.dumps(person))

# with open('test.json', 'w+') as file:
#     json.dump(person, file)
#     file.seek(0)
#     file.read()

# from package_ import file_module

# from package_.file_module import sum_file

# from package_ import file_module as f
# f.sum_file

''' import '''
# import module_name as псевдоним
# from module/packet import ... [as псевдоним]

# from package_ import hello
# print (hello.hello)

# from package_.hello import hello
# print (hello)

# from package_ import file_module
# file_module.sum_file(4,67)

# from package_.my_package import file1
# file1.print2()

# from math import babbasbdabsdbasb as b

# изучаем CSV