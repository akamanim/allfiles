""" ================================= """
""" ========================================== Цикл ========================================"""
""" ================ while -> Работает до того времени, пока условие True ================= """
''' '''
# while True:
    # print ('i') # Бесконечное условие, опасно!!!
 
 
# counter = 0 
# while counter < 11:
#     print (counter)
#     counter = counter +1

# while False: Никогда не заработает
# counter = 10
# while counter > 0:
#     print (counter)
#     counter = counter -1

# a = 0 
# while a:
#     print ('hell0')
# print (bool(a)) ## Не работает вообще.

# n = 555
 
# suma = 0
# mult = 1
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10
 
# print("Сумма:", suma)

# # a = 115
# summa = 0
# for i in str(a):
#     summa = summa + int(i)
# print (summa)

# a = '1bg3g4yhy7f9ads'
# summa = 0
# for i in a:
#     if i.isdigit():
#            summa = summa + int(i)
# print (summa)

# i = 0
# a = str(1231231313)
# summa = 0
# while i < len(str(a)):
#     # print (str(a)[i])
#     summa = summa + int((a[i]))
#     i = i + 1

dict_ = {'a': 1, "b": 2, 'c' : 3, 'd': 4}
# for i in dict_: 
#     print(i)
##  при иттерации словаря -> Получаем только ключи


# for i in dict_.keys():           -> Прохождение по ключам 
# #     print (i)


# for i in dict_.values():          -> Прохождение по значениям
#     print (i)

# for i in dict_.items():            -> получаем Tuple из ключа и значения
    # print (i)

# for k, v in dict_.items():          -> Ключи и значения получать по отдельности
    # print (k)
    # print (v)

# for a,b,c in [(1,2,3), (4,5,6), (7,8,9)]: #-> Множественное присвоение 
    # print (f'Числа a: {a},Числа b: {b}Числа c: {c}')

""" ================ Ключевые слова в циклах ================= """
''' break -> полностью выйти из цикла. досрочно прерывает цикл'''
''' continue -> переход к следующей итерации '''
''' Оператор continue -> начинает следующий проход к цикла, при этом минуя ставшеся тело цикла '''

# for i in 'hello': 
    # Тело

# for i in range(1,102):
#     if i % 2 == 1: ## Перешагивает 
#         continue
#     print (i)

# for i in range(1,102):
#     if i > 10:
#         break
#     print (i)

# i = 0
# while i < 10:
#     # i = i + 1
#     i += 1 
#     if i == 3:
#         continue
#     elif i == 7:
#         break
#     print (i)

''' ========== else ========='''
''' слово else, применяется в циклах for и while -> проверяет, был ли произведен выход из цикла без инструкции break '''
# i = 0
# while i < 10:
#     if i == 5: pass
#     print(i)
#     i+=1
# else:
#     print ('hello')
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# hello

'''========== Оператор pass ========='''

# for i in range(1,102):
#     if i > 10:
#         pass
#     print (i)
''' ключевое слово pass – самостоятельная инструкция, которая буквально ничего не делает. '''