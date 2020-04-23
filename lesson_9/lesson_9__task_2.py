"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter, deque


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree(data):
    meta = Counter(data)
    data = deque(sorted(meta.items(), key=lambda x: x[1]))

    while len(data) > 1:

        value = data[0][1] + data[1][1]
        left=data.popleft()[0]
        right=data.popleft()[0]
        node = Node(value, left, right)

        for name, item in enumerate(data):

            if value > item[1]:
                continue
            else:
                data.insert(name, (node, value))
                break

        else:
            data.append((node, value))

    return data[0][0]


def rule(tree, data=dict(), meta=''):
    node = tree
    meta = meta
    data = data
    
    if not isinstance(node, Node):
        data[node] = meta
    else:
        rule(node.left, data, f'{meta}0')
        rule(node.right, data, f'{meta}1')
    
    return data


def code(data, rule):
    meta = data
    temp = rule
    data = ''

    for item in meta:
        data += temp[item]

    return data


def text(data, rule):
    meta = data
    temp = rule
    data = ''
    step = 0

    while step < len(meta):

        for item in temp:

            if meta[step:].find(temp[item]) == 0:
                data += item
                step += len(temp[item])

    return data


data = 'beep boop beer!'
meta = rule(tree(data))
assert data == text(code(data, meta), meta), "Результат декодирования не совпадает с оригинальным значением."

print(f'\nОригинальная строка: {data}')
print(f'\nЗакодированная строка: {code(data, meta)}')
print('\nКодирование:')
for char, code in meta.items():
    print(f'    {char}: {code}')
print()
