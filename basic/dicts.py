"""==================================== Тип данных Словари dict() =========================="""
"""================================="""
''' {key: value} '''
''' позволяет хранить  любые обьекты, для доступа к которым используется ключ (key) '''
''' Этот тип данных является: Изменяемым, итерируемым, неиндексируемый, упорядочный '''

# {} -> Литералы
# dict_ = {}
# print (type(dict_))

# dict_ = {'a': 'Hello', 'b': 'world', 'c': 3}
# print (dict_['a']+ dict_['b'])
''' Ключи должны быть неизеняемыми типами данных '''
''' Ключи должны быть уникальными '''
''' значениями словаря могут быть любые типы данных '''

# dict_ = {{1;1}: 'hello'} TypeError: unhashable type: 'dict'
# dict+ = {1: {'a':'one'}, 'hello': [1,2,3]}

# dict_ = {'a': 1, 'a':2, 'a':3}
# print (dict_)
# dict_['a'] = 100
# print(dict_)

"""================ Создание словарей ================="""
# 1. {key: value}
# 2. dict()
# print (dict('hello')) #ERROR
# print (dict([('key1', 'value1'), ('key2', 'value2')]))
# print(dict(['ad','bc','lk']))

# key1, value1 = '1a' # 1-ый элемент относится к первой переменной, а второй к второй
# print (key1,value1)
 
# print (dict(a='hello', b = 'hello'))

"""================ Методы словарей ================="""
dict_ = {'name':'Volvo', 'age': 95, 'hobby': ['footbal', 'poker', 'sing']}
''' .clear() -> Очищает словарь -> {} '''
# dict_.clear()
# print (dict_)

''' .copy() -> возвращает копию словаря '''
# dict_2 = dict_.copy()
# dict_2 ['hobby'][0] = 'BasketBall' # Изменится и в род переменной. 
# dict_2 ['hobby'] = 'hi' # Вот так правильно использовать copy
# print (dict_2)
# print (dict_)

''' deepcopy '''
# from copy import deepcopy 
# dict_2 = deepcopy(dict_)
# dict_2 ['hobby'][0] = 'hi'
# # dict_2 ['hobby'] = 'hi'
# print (dict_2) ## {'name': 'Volvo', 'age': 95, 'hobby': ['hi', 'poker', 'sing']}

''' dict.fromkeys(seq, [value]) -> создает словарь, с ключами из seq и значением value(для всех одинаковый, по умолчанию None) '''
# list_ = ['name', 'age', 'hobby']
# dict_ = dict.fromkeys(list_,'bob') 
# print (dict_) ## {'name': 'bob', 'age': 'bob', 'hobby': 'bob'}

''' Получение элементов из словаря '''
''' .get(key, [value]) -> Будет возвращать значение по ключу '''
# print (dict_.get('name2','no such')) ## no such (Если такого ключа нет(Value))
# print (dict_.get('name'))  ## Volvo
# print(dict_['dnjks'])

''' Изменение элементов словаря '''
# dict_['name'] = 'sam' # (Изменение пары)
# dict_['address'] = 'Belinka 4' ## {'name': 'sam', 'age': 95, 'hobby': ['footbal', 'poker', 'sing'], 'address': 'Belinka 4'} (создание новой пары)
# dict_['hobby'].append('VoleyBall') ## hobby': ['footbal', 'poker', 'sing', 'VoleyBall']0
# print (dict_)

''' .update(new_dict) -> Добавляет новый словарь(new_dict), в ныне существующий '''
# new_dict = {'City': 'Bishkek'}
# dict_.update(new_dict)
# print (dict_) ## {'name': 'sam', 'age': 95, 'hobby': ['footbal', 'poker', 'sing', 'VoleyBall'], 'address': 'Belinka 4', 'City': 'Bishkek'} # Добавляет новую пару в конец.

''' .setdefault(key, [default_value]) -> Работает точно так же как метод get(), но если нет такой пары, создаст новую (key: default_value)'''
# dict_.setdefault("country", 'Kyrgyzstan')
# print (dict_) ## {'name': 'Volvo', 'age': 95, 'hobby': ['footbal', 'poker', 'sing'], 'country': 'Kyrgyzstan'} Создание новой пары
# print (dict_.setdefault('name')) ## Volvo

''' .keys() -> Выводит в терминал все ключи '''
# print (dict_.keys()) ## dict_keys(['name', 'age', 'hobby']) 

''' .values() -> Выводит в терминал все значения '''
# print (dict_.values()) ## dict_values(['Volvo', 95, ['footbal', 'poker', 'sing']])

''' .items() -> Возвращает все пары из словаря '''
# print (dict_.items()) ## ('name', 'Volvo'), ('age', 95), ('hobby', ['footbal', 'poker', 'sing'])

"""================ Удаление элементов словарей ================="""

''' pop(key, [messege]) -> Удаляет пару ключ и значение, и возвращает удаленное значение '''
''' Если ключа нет, возвращает messege, по умолчанию, бросает исключение(ERROR)'''
# print (dict_.pop('GOod', 'UPS')) ## UPS
#                               {'name': 'Volvo', 'age': 95, 'hobby': ['footbal', 'poker', 'sing']}
# print (dict_)
''' .popitem() -> Удаляет и возвращает  удаляет последнюю добавленую пару '''
# print (dict_.popitem())
# print (dict_) ## {'name': 'Volvo', 'age': 95}
count = 0 
print (count)