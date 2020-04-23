"""
Определение количества различных подстрок с использованием хеш-функции. Пусть 
на вход функции дана строка. Требуется вернуть количество различных подстрок 
в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой 
  другой из модуля hashlib) задача считается не решённой.
"""

import hashlib


def count(text):
    meta = str(text).lower()
    size = len(meta)
    data = set()

    for temp in range(1, size):

        for item in range(size - temp + 1):
            code = hashlib.sha1(meta[item : item + temp].encode('utf-8')).hexdigest()
            data.add(code)
        
    return len(data)


data = input('Строка, для определения количества различных подстрок в ней: ')
assert count('hello') == 13, 'Функция работает не корректно.'

print(f'Количество различных подстрок в строке "{data}": {count(data)}')
