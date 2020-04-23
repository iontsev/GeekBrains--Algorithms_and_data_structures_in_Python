"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом 
каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] 
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def summation_hex(x, y):
    meta = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    data = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            item = meta[x.pop()] + meta[y.pop()] + transfer
        else:
            item = meta[x.pop()] + transfer

        transfer = 0

        if item < 16:
            data.appendleft(meta[item])
        else:
            data.appendleft(meta[item - 16])
            transfer = 1

    if transfer:
        data.appendleft('1')

    return list(data)


def multiplication_hex(x, y):
    meta = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    data = deque()
    temp = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = meta[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            temp[i].appendleft(m * meta[x[j]])

        for _ in range(i):
            temp[i].append(0)

    transfer = 0

    for _ in range(len(temp[-1])):
        item = transfer

        for i in range(len(temp)):
            if temp[i]:
                item += temp[i].pop()

        if item < 16:
            data.appendleft(meta[item])
        else:
            data.appendleft(meta[item % 16])
            transfer = item // 16

    if transfer:
            data.appendleft(meta[transfer])

    return list(data)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(a, b)
print(*a, '+', *b, '=', *summation_hex(a, b))
print(*a, '*', *b, '=', *multiplication_hex(a, b))
