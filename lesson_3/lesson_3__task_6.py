"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и 
максимальным элементами. Сами минимальный и максимальный элементы в сумму 
не включать.
"""

from random import randint


n = 20
min_id = 0
max_id = 0
a = [randint(0, 100) for _ in range(n)]

for i in range(len(a)):

    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i

if min_id > max_id:
    min_id, max_id = max_id, min_id

data = 0

for i in range(min_id + 1, max_id):
    data += a[i]

print(f'Массив: {a}')
print(f'Минимальный элемент в массиве: {a[min_id]}')
print(f'Максимальный элемент в массиве: {a[max_id]}')
print(f'Сумма элементов между минимальным и максимальным элементами: {data}')
