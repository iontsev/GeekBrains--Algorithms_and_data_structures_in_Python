"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный 
и отсортированный массивы.
"""

import random


def sort(data):


    def merge(first, last):
        data = []
        i, j = 0, 0

        while i < len(first) and j < len(last):

            if first[i] < last[j]:
                data.append(first[i])
                i += 1
            else:
                data.append(last[j])
                j += 1

        data.extend(first[i:] if i < len(first) else last[j:])

        return data


    def split(data):

        if len(data) == 1:
            return data
        elif len(data) == 2:
            return data if data[0] <= data[1] else data[::-1]
        else:
            return merge(split(data[:len(data)//2]), split(data[len(data)//2:]))


    return split(data)


size = 10
data = [random.randint(0, 49) for item in range(size)]

print(f'Массив до сортировки:\n{data}\n')
data = sort(data)
print(f'Массив после сортировки:\n{data}\n')
