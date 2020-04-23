"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его 
на две равные части: в одной находятся элементы, которые не меньше медианы, 
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это 
слишком сложно, используйте метод сортировки, который не рассматривался 
на уроках (сортировка слиянием также недопустима).
"""

import random


def find_median(data):
    meta = list(data)
    temp = []

    for test in meta:
        less = 0
        same = 0
        more = 0

        for item in meta:

            if item < test:
                less += 1
            elif item > test:
                more += 1
            else:
                same += 1

        if abs(less - more) < 1 + same:
            temp.append(test)

    temp = set(temp)

    if len(temp) > 0:
        data = sum(temp) / len(temp)
        data = int(data) if data % int(data) == 0 else float(data)
    else:
        data = None

    return data


def view_median(data):
    meta = sorted(list(data))
    size = len(meta)
 
    if size % 2 == 0:
        data = (meta[size // 2] + meta[size // 2 - 1]) / 2
        data = int(data) if data % int(data) == 0 else float(data)
    else:
        data = meta[size // 2]

    return data


m = random.randint(5, 10)
size = 2 * m + 1
data = [random.randint(0, 50) for item in range(size)]

print(f'Сгенерирован массив из 2 * {m} + 1 = {size}  элементов:\n{data}')
print(f'Медиана: {find_median(data)}')

# print('\nПроверка:')
# print(f'Отсортированный массив:\n{sorted(data)}')
# print(f'Медиана: {view_median(data)}')
