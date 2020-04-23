"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных 
в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:
    a. выбрать хорошую задачу, которую имеет смысл оценивать,
    b. написать 3 варианта кода (один у вас уже есть),
    c. проанализировать 3 варианта и выбрать оптимальный,
    d. результаты анализа вставить в виде комментариев в файл с кодом 
       (не забудьте указать, для каких N вы проводили замеры),
    e. написать общий вывод: какой из трёх вариантов лучше и почему.


Выбрана задача 4 из урока 3:
Определить, какое число в массиве встречается чаще всего.
"""

from cProfile import run as profile
from random import randint as random


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

    return item

# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_1([random.randint(0, 5) for _ in range(10)])"
# 100 loops, best of 5: 42.5 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_1([random.randint(0, 50) for _ in range(100)])"
# 100 loops, best of 5: 1.15 msec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_1([random.randint(0, 500) for _ in range(1000)])"
# 100 loops, best of 5: 103 msec per loop
# 
# 
# profile('variant_1([random(0, 5) for _ in range(10)])')
# 68 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:22(variant_1)
# 
# profile('variant_1([random(0, 50) for _ in range(100)])')
# 633 function calls in 0.003 seconds
# 1    0.002    0.002    0.002    0.002 lesson_4__task_1.py:22(variant_1)
# 
# profile('variant_1([random(0, 500) for _ in range(1000)])')
# 6027 function calls in 0.158 seconds
# 1    0.148    0.148    0.148    0.148 lesson_4__task_1.py:22(variant_1)
# 
# Время выполнения нарастает. Рекурсий нет.
# Предположительно, алгоритм сложности O(n**3).


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

    return item

# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_2([random.randint(0, 5) for _ in range(10)])"
# 100 loops, best of 5: 31.4 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_2([random.randint(0, 50) for _ in range(100)])"
# 100 loops, best of 5: 294 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_2([random.randint(0, 500) for _ in range(1000)])"
# 100 loops, best of 5: 3.1 msec per loop
# 
# 
# profile('variant_2([random(0, 5) for _ in range(10)])')
# 62 function calls in 0.001 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:70(variant_2)
# 
# profile('variant_2([random(0, 50) for _ in range(100)])')
# 530 function calls in 0.001 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:70(variant_2)
# 
# profile('variant_2([random(0, 500) for _ in range(1000)])')
# 5031 function calls in 0.005 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:70(variant_2)
# 
# 
# Время выполнения нарастает. Рекурсий нет.
# Предположительно, алгоритм сложности O(n).


def variant_3(data):

    if len(data) == 0:
        return None

    temp = {i: 0 for i in data}

    for i in data:
        temp[i] += 1

    rate = max(temp.values())
    item = {k: v for k, v in temp.items() if v == rate}

    return list(item.keys())[0]

# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_3([random.randint(0, 5) for _ in range(10)])"
# 100 loops, best of 5: 33.7 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_3([random.randint(0, 50) for _ in range(100)])"
# 100 loops, best of 5: 284 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_1" "import random" "lesson_4__task_1.variant_3([random.randint(0, 500) for _ in range(1000)])"
# 100 loops, best of 5: 3.09 msec per loop
# 
# 
# profile('variant_3([random(0, 5) for _ in range(10)])')
# 63 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:117(variant_3)
# 
# profile('variant_3([random(0, 50) for _ in range(100)])')
# 535 function calls in 0.001 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:117(variant_3)
# 
# profile('variant_3([random(0, 500) for _ in range(1000)])')
# 5038 function calls in 0.005 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_1.py:117(variant_3)
# 
# 
# Время выполнения нарастает. Рекурсий нет.
# Предположительно, алгоритм сложности O(n).


# ВЫВОД:
# Алгоритм variant_1 самый затратный по времени. 
# Сложность алгоритмов variant_2 и variant_3 и время их работы приблизительно одинаковые.
# Предпочтителен variant_3 (третий вариант) предпочтителен из-за скорости, и возможности 
# легко его изменить под вывод всех вариантов ответа (когда максимальная частота 
# у нескольких элементов).


# size = 20
# data = [random(0, size // 2) for _ in range(size)]
# print(data)
# print(variant_1(data))
# print(variant_2(data))
# print(variant_3(data))
