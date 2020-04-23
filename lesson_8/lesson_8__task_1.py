"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям 
(по одному разу). Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
"""

def graph(size):
    data = [[0 if line == item else 1 for item in range(size)] for line in range(size)]

    return data


def count(data):
    meta = data
    data = 0

    for i, line in enumerate(meta):

        for j, item in enumerate(line):

            if i < j:
                data += item

    return data


n = int(input('Количество друзей: '))
print(f'Количество руковожатий: {count(graph(n))}')
