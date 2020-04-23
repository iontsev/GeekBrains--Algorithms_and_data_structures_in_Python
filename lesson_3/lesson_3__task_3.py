"""
В массиве случайных целых чисел поменять местами минимальный и максимальный 
элементы.
"""

from random import randint


n = 20
min_id = 0
max_id = 0
a1 = [randint(0, 100) for _ in range(n)]
a2 = list(a1)

for i in range(len(a1)):

    if a1[i] < a1[min_id]:
        min_id = i
    elif a1[i] > a1[max_id]:
        max_id = i

swap = a2[min_id]
a2[min_id] = a2[max_id]
a2[max_id] = swap
 
print(f'Исходный массив: {a1}')
print(f'Минимальный элемент в массиве: {a1[min_id]}')
print(f'Максимальный элемент в массиве: {a1[max_id]}')
print(f'Итоговый массив: {a2}')
