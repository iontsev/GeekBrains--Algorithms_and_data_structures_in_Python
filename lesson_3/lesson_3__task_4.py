"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint


n = 20
a = [randint(0, 10) for _ in range(n)]

item = a[0]
max_rate = 1

for i in range(len(a) - 1):
    rate = 1

    for j in range(i + 1, len(a)):

        if a[i] == a[j]:
            rate += 1

    if rate > max_rate:
        max_rate = rate
        item = a[i]
 
print(f'Массив: {a}')

if max_rate > 1:
    print(f'Чаще всего встречено число {item}')
else:
    print('Все элементы уникальны')
