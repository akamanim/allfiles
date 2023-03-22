''' =========================== Обработка исключений ============================= '''
''' Ошибка -> проблема в синтаксисе (котороые исправляем самостоятельно) '''
''' 1. SyntaxError -> забыли поставить двоеточие, ковычку, скобку и так далее '''
''' 2. IndentationError -> Не правильный отступ '''
''' SyntaxInvalid - 2f = 8 '''
''' 3. TabError -> неверная табуляция (смешивание пробелов и табов) '''

''' ========================= Исключения ========================== '''
''' 1. NameError ->  '''
''' 2. IndexError ->  '''
''' 3. ZeroDivisionError ->  '''
'''        ArithmeticalError -> '''
''' 4. KeyError -> '''
''' 5. ImportError ->  '''
''' 6. ValueError -> '''
''' 7. TypeError -> '''
''' 8. AttributeError -> '''
''' 9. BaseException(прородитель) -> '''

NameError # Исключение, которое выходит, когда мы обращаемся к несуществующему имени
IndexError # Выходит, когда обращаемся к несуществующему индексу
ZeroDivisionError # выходит, при делении на ноль.
KeyError #  Выходит, когда обращаемся к несуществующему ключу
ImportError # Вызов несуществующего Импорта
ValueError # когда пытаемся распаковать последовательность, где кол-во элементов и переменных не совпадают(a,b,c='ab').Или когда в функцию передаем не корректный тип данных (int('bob'))
TypeError #  возникающее при попытке манипуляции объектом не поддерживающим такого рода манипуляцию.
AttributeError # Возбуждается в случаях ошибок доступа к атрибуту, либо его установки.
BaseException # когда обращаемся к несущестующему атрибуту или методу обьекта.

''' ====================== Обработка исключений ======================'''
""" Что-бы код не прекращал работать при некорректных данных """
# try: 
#     '''code, which can call a error '''
# except (error, which can be):
#     ''' code, which will be work, if in try was a error '''
# else: 
#     ''' code, will work, if in 'try' not be error '''
# finally: 
#     ''' code,which will be work in all situation '''
''' ================================================= '''
# try:
#     a = int(input('Введите число - '))
# except ValueError:
#     try:
#         a = int(input('Введите только символы! - '))
#     except ValueError:
#         print ('Идите в жопу')
''' ================================================= '''
# try: 
#     print (10 / 0)
# except ZeroDivisionError:  
    # print ('Ошибка, деление на ноль')
''' ================================================= '''
# try:
#     while True:
#         print(0)
# except KeyboardInterrupt:
#     print ('ctrl+c')
''' ================================================= '''
# try: 
#     num1 = int(input('Введите число - '))
#     num2 = int(input('Введите число - '))
#     print (num1/num2)
# except ZeroDivisionError:
#     print ('Деление на ноль!')
# except ValueError:
#     print ('Неправильное действие!')
''' ================================================= '''
# try: 
#     print (10 / 0)
# except: # Обработка всех исключений 
#     print ('Ошибка, деление на ноль')
''' ================================================= '''
# try:
#     dict_ = {key:key**2 for key in range(100) if key % a == 0}
# except NameError:
#     a = 2
#     dict_ = {key:key**2 for key in range(100) if key % a == 0}
# print (dict_)
''' ========================= else в обработке исключения ======================== '''
# try:
#     dict_ = {'a':4, 'b':10}
#     key_ = input ('Введите ключ: ')
#     res = dict_[key_]
# except Exception as e:
#     print (f'Нет такого ключа {e}')
#     print (f'Существующие ключи {dict_.keys()}')
# else:
#     print ('Block else')
''' =============================================================================== '''
''' Finally block in try except '''
# try:
#     res = a*2
#     print (res)
# except Exception as e:
#     print (f'Возникла ошибка {e.__class__}')
# else:
#     print (res)
# finally:
#     a = 5
#     res = a*2
#     print (res)

''' raise -> Исскуственно вызывает ошибку '''
n = int(input("Введите число - "))
if n <= 0:
    raise ValueError('Че лепишь, на?')

try:
    if 2 > 1:
        raise Exception('f')
except:
    print ('Че нах')