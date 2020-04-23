"""
Написать программу, которая обходит не взвешенный ориентированный граф 
без петель, в котором все вершины связаны, по алгоритму поиска в глубину 
(Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход 
   число вершин.
"""

from random import randint as random


def graph(size):
    data = [[0 if line == item else random(0, 1) for item in range(size)] for line in range(size)]

    print()
    print('Сгенерирован граф: ')
    for line in data:

        for item in line:
            print(f'\t{item}', end='')

        print()

    print()

    return data


def dfs(graph, start=0):
    meta = graph
    temp = [start]
    data = [start]

    while len(temp) > 0: 
        line = temp.pop()

        for name, item in enumerate(meta[line]):

            if item > 0 and name not in data:
                data.append(name)
                temp.append(name)

    return data


size = int(input('Количество вершин в графе: '))
name = random(0, size -1)
data = graph(size)

print(f'Пройдены вершины, начиная с индекса "{name}": ')

for item in dfs(data):
    print(f'\t{item}', end='')

print()
