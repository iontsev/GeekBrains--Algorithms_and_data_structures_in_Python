"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных 
программах в рамках первых трех уроков. Проанализировать результат и 
определить программы с наиболее эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением 
будет:
a.  выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b.  написать 3 варианта кода (один у вас уже есть);
    проанализировать 3 варианта и выбрать оптимальный;
c.  результаты анализа (количество занятой памяти в вашей среде разработки) 
    вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d.  написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof 
после каждой переменной, а проявили творчество, фантазию и создали 
универсальный код для замера памяти.

Выбрана задача 4 из урока 3:
Определить, какое число в массиве встречается чаще всего.
"""

import sys
from random import randint as random

# Тесты выполнены на 64-разрядной Win 10 версии 1916
# Python 3.8.2 [MSC v.1916 64 bit (AMD64)] on win32
print(sys.version, sys.platform)


def show_size(data, show=False, step=0):
    meta = 0

    for item in data:

        if show == True:
            print(f'\nПеременная: {item}')
            print(f'Весит: {sys.getsizeof(item)}')
        
        temp = sys.getsizeof(item)

        if hasattr(item, '__iter__') and not isinstance(item, str):

            if hasattr(item, 'keys'):

                for key, value in item.items():

                    if  show == True:
                        print(f'\nКлюч: \'{key}\' значение {value}')

                    temp += show_size([key], show, step + 1) + show_size([value], show, step + 1)

            else:
                temp += show_size(item, show, step + 1)

        meta += temp

    if step == 0 or show == True:
        print(f'Переменные: {data}')
        print(f'Затраты памяти программы: {meta}')

    return meta


def variant_1(data):

    if len(data) == 0:
        return None

    item = data[0]
    rate = 1

    for i in range(len(data) - 1):
        temp = 1

        for k in range(i + 1, len(data)):

            if data[i] == data[k]:
                temp += 1

        if temp > rate:
            rate = temp
            item = data[i]

    _variable = []

    for i in dir():

        if i[0] != '_' and not hasattr(locals()[i], '__name__'):
            _variable.append(locals()[i])

    show_size(_variable)

    return item



def variant_2(data):
    
    if len(data) == 0:
        return None

    temp = dict.fromkeys(set(data), 0)

    for i in data:
        temp[i] += 1
    
    item = data[0]
    rate = temp[item]

    for k, v in temp.items():

        if rate < v:
            item = k

    _variable = []

    for i in dir():

        if i[0] != '_' and not hasattr(locals()[i], '__name__'):
            _variable.append(locals()[i])

    show_size(_variable)

    return item


def variant_3(data):

    if len(data) == 0:
        return None

    temp = {i: 0 for i in data}

    for i in data:
        temp[i] += 1

    rate = max(temp.values())
    item = {k: v for k, v in temp.items() if v == rate}

    _variable = []

    for i in dir():

        if i[0] != '_' and not hasattr(locals()[i], '__name__'):
            _variable.append(locals()[i])

    show_size(_variable)

    return list(item.keys())[0]


# Cобираем переменные и подсчитываем затрачиваемую память.

# size = 10
# data = [random(0, size // 2) for _ in range(size)]
data = [4, 5, 1, 3, 4, 4, 5, 3, 4, 2]

print('\nВариант 1')
variant_1(data)
# Затраты памяти программы: 578

print('\nВариант 2')
variant_2(data)
# Затраты памяти программы: 1090

print('\nВариант 3')
variant_3(data)
# Затраты памяти программы: 1294

# ВЫВОД:
# Вариант 1 - показал лучшие результаты по затратам памяти.
# Вариант 3 - считаю лучшим по сочетанию функциональности, читаемости и 
# производительности.
