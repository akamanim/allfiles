"""======================================== строки(STRINGS) ================================================"""
# строки -> неизменяемый тип данных, который представляет последовательность символов, заключенных в кавычки
                            # id() -> возвращает номер ячейки памяти 
# a = '5'
# b = 5
# print (id(a))
# # print (id(b))
# a = "hello"
# b = "hola"
# print (id(a))
# print (id(b))
                            # string =  'строка с одинарными ковычками '
                            # string2 =  "строка с двойными ковычками"
                            # string3 =  'не правильный синтаксис, ковычки должны быть одинаковыми"

# string4 = " don't, 'book', 'dsa' "
# string = """
# book 
# look
# """
# print (string)


                             #len () ->  возвращает кол-во символов в строке

# print (len('string'))                      
"""======================================= Экранизация строк ====================================="""
                            # '\символ'

'\n' # -> Перенос на след строку
# a = 'hello \nworld'
# print (a)

'\t' # -> табуляция
# a = 'hello\tworld'
# print (a)

'\\' # -> для отображения '\'    
' \' ' # -> для отображения '   
' \" ' # -> для отображения "
'\r' # -> возвращение каретки в начало строки
'\v' # -> перенос на новую строку со смещением вправо на кол-во символов предыдущего слова
# print ('hello\vworld')
'\a' # -> гудок(заставлял ноут-бук писщать)
# print ('hello\a')

"""=========================== Конкатенация строк -> склеивание строк ============================="""
# a = "hello"
# b = 'world'
# print (a + b)

# print ('hello ' * 5)   #console: hello hello hello hello hello "Дублирование строки"

"""========================= Формитирование строк (Динамические строки) =========================="""

                            # 1. %
                            # 2. .format()
                            # 3. f-строки
#1
# name = input ('Введите имя: ')
# print ('Hello, %s' %name )

#2 
# name = input ('Введите имя: ')
# name2 = input ('name2: ')
# print ('Hello, {}, {},'.format(name, name2))

#3 Интерполяция строк
# name = input ('Введите имя: ')
# name2 = input ('name2: ')
# print (f'Hello {name}, {name2}')

#print (dir('s'))

"""======================================= Методы строк ====================================="""
                        # Методы -> функции, к которым мы обращаемся через точку

                            # Методы на is проверяют результаты True/False
# name.isdigit() -> проверяет, состоит ли наша строка только из чисел.(True)
# name.isalnum() -> проверяет, состоит ли наша строка только из букв или чисел.(True)
# name.isalpha() -> проверяет, состоит ли наша строка только из букв.(True)
# name.islower() -> проверяет, записаны ли все символы строки в нижнем регистре.(True)
# name.isupper() -> проверяет, записаны ли все символы строки в верхнем регистре.(True)
# name.isspace() -> проверяет, есть ли в нашей строке неотображаемые символы (пробел, '\n' ...)


                        # .lower() -> переводит целую строку в нижний регистр
# print ("ASDldasLLA" .lower())
                        # .upper() -> переводит целую строку в верхний регистр
# print ("ASDldasLLA" .upper())        
                        # .swapcase() -> переводит символы в противоположный регистр
# print ("AAAbbbAAAA" .swapcase())   
                        # .title() -> переводит первую букву каждого слова в верхний регистр
# print ("good morning" .title())
                        # .capitalize() -> переводит первый символ в верхний регист
# print ("good morning" .capitalize())
                        # .strip() -> Убирает пробел в начале строки и в конце строки.
# print ("   My school, you go to     " .strip())
                        # .lstrip() -> Убирает пробельные символы в начале строки
                        # .rstrip() -> Убирает пробельный символы в конце строки
                        # .replace(old, new, [count]) -> меняет старое значение(old) на новое(new) кол-вом(count)
# print ("ha ha ha ha" .replace('ha', 'new', 2))
                        # .split(разделитель) -> Делит нашу строку по разделителю и возвращает массив
                        # .split() -> Меняет тип данных (Строку-Массив)
# print ("hello py27 python even" .split('y'))
                        # разделитель.join(iterable) -> соединяет в строку по разделителю
# a = "hello py27 python even"
# list_ = a.split()
# print (list_)
# print ('-->'.join(list_))
                        # .startswith(string) -> проверяет начинается ли наша строка с string
# a = 'hello world'
# print (a.startswith('hel'))
                        # .endswith(string) -> проверяет заканчивается ли наша строка с string   
# a = 'hello world'
# print (a.endswith('rld'))       
                        # .count(string) -> считает кол-во вхождений string в строке
# a = 'llooffddssccf'
# print (a.count('ll'))

"""======================================= Индекс ====================================="""
                      #Индекс порядковый номер элемента, всегда начинается с 0 
'hello'
#01234
# a = 'hello world'
# print (a[5])
# print (a[-1])
# ...-3-2-1
"""---- СРЕЗЫ ----"""
# a[start:stop]
                    # срезы по индексу -> нахождение подстроки, при этом начиная от start'а и заканчивая до stop'a,(stop не включительно), шаг - через какой элемент записывать
# print (a[0:3])
# print (a[0::3])
# a = 'hello world'
# print (a[::-1])

# string = 'Hello World'
# print (string.split(' '))

m = int(input())
if m == 1 or m == 2 or m == 12:
    print ('Зима')
elif m == 3 or m == 4 or m == 5:    
    print ("Весна")
elif m == 6  or m == 7 or m == 8:
    print ("Лето")
elif m == 9 or m == 10 or m == 11:    
    print ("Осень")
else: 
    print ('Такого месяца нет')