''' ================ Множества set() =================='''
''' Изменяемый, не упорядочный, итерируемый, неиндексируемый '''
''' В основном предназначен для хранения уникальных вещей '''
''' Элементами множеств, могут быть только не изменяемые типы данных'''
''' Если используете tuple, то в них тоже должны храниться неизменяемые типы данных '''

# set1 = {1, 2, 3,}
# print (set1)
# for i in set1:
#     print (i)

# set2 = {4,5,6,7,(1,2,3), 1,2,3} 
# print (set2) ## {1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}

# set3 = {1,True,0,False}
# print (set3) ## {0, 1}

''' ===================== Создание множеств ====================== '''
# a = set(({'a':1})) ## Выведет только ключи
# print (a)

# a = set('hello world') 
# print (a) ## {'l', ' ', 'r', 'e', 'w', 'H', 'd', 'o'}

# set_ = {1,2,3,'helli', (4,5),None,False}
# print (set_) ## {False, 1, 2, 3, None, 'helli', (4, 5)}

''' =============================== Методы множеств ================================ '''
''' Добавление элемента '''
''' .add(element) '''
# set_ = {1,2,3}
# set_.add(4)
# print (set_) ## {1, 2, 3, 4}
# set_.add('hello')
# print (set_) ## {'hello', 1, 2, 3}
# set_.add((1,2,3))
# print (set_) ## {1, 2, 3, 4, 'hello', (1, 2, 3)}
# set_.add([1,2,3])
# print (set_) ## ERROR TypeError: unhashable type: 'list'
''' .update(sequence) -> ( За раз может добавить несколько элементов, но не повторяется)'''
''' Передаем все итерируемые '''
set_ = {1, 2, 3}
# set_.update('hello')
# print (set_) ## {1, 2, 3, 'e', 'h', 'l', 'o'}
# set_.update([1,2,3,4])
# print (set_) ## {1, 2, 3, 'e', 4, 'o', 'h', 'l'}
set_.update ({'assa': 2,'baasa':3},'string')
# print (set_) ## {1, 2, 3, 'o', 4, 'g', 'baasa', 'i', 'n', 'e', 't', 'l', 's', 'h', 'r', 'assa'}
''' ================================= Методы удаления ================================= '''
''' .clear() -> Очищение всего множества '''
# set_.clear()
# print (set_) ## set()
''' .remove(element) -> Удаляет элемент, если такого элемента нет, то дает ошибку '''
# set_.remove(1) ## {2, 3, 'baasa', 'assa', 'n', 't', 'i', 's', 'r', 'g'}
''' .discard(element) -> Также удаляет элемент, если элемента нет, то ошибку не выдает. '''
# set_.discard(None) ## Ошибку не выдает!
''' .pop() -> Удаляет случайный элемент, так же удаляет, самого начала, но set выдает в разнобой '''
# set_.pop() ## {2, 3, 'assa', 'baasa', 't', 'g', 'n', 'i', 's', 'r'}
# print (set_)

''' set_a.difference(set_b) -> выводит элементы, которые есть в set_a, но нет в set_b '''
# set_a - set_b
# set_a = {1,2,3}
# set_b = {3,4,5,6}
# print (set_a.difference(set_b))
# print (set_a - set_b) ## {1, 2}

''' .symmetric_difference -> Выводит уникальные элементы в обоих множествах '''
# set_a = {1,2,3}
# set_b = {3, 4, 5, 6}
# print(set_a.symmetric_difference(set_b)) ## {1, 2, 4, 5, 6}
# print ((set_a ^ set_b)) ## {1, 2, 4, 5, 6}

''' .intersecrion -> Выводит одинаковые элементы '''
# set_a = {1,2,3}
# set_b = {3, 4, 5, 6}
# print (set_a.intersection(set_b)) ##{3}
# print ((set_a & set_b))  ##{3}

''' .union -> Обьеденение(соединяет set_a + set_b)'''
# set_a = {1,2,3}
# set_b = {3, 4, 5, 6}
# print (set_a.union(set_b)) ##{1, 2, 3, 4, 5, 6}
# print ((set_a | set_b))  ##{1, 2, 3, 4, 5, 6}

'''
Домашнее задание
# copy()
# difference_update()
# intersection_update()
# symmetric_difference_update()
# ИЗУЧИТЬ ЭТИ МЕТОДЫ
'' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' 
# isdisjoint()
# issubset()
# issuperset()
# ИЗУЧИТЬ ЭТИ МЕТОДЫ!!!!
# '''
# a = [1,2,3,4]
# for i in a:
#     print(i)
#     a.append(i)

# a = "1.1.1.1"
# print (a.replace('.', '[.]'))

# for i in a: 
#     if i == '.':
#         i = '[.]'
#     a += i
# print(a)

# command = 'g()()()(al)'
# print(command.replace('()',"o").replace('(al)','al'))

# a = {0,1,111}
# b = {0,1,2,3,34,5,8,13}
# print (a.intersection(b))
