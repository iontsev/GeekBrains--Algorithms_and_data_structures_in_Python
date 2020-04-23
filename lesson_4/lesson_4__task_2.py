"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция 
нахождения простого числа должна принимать на вход натуральное и возвращать 
соответствующее простое число. Проанализировать скорость и сложность 
алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. 
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
>>> sieve(2)
3
>>> prime(4)
7
>>> sieve(5)
11
>>> prime(1)
2

Примечание по профилированию кода: для получения достоверных результатов 
при замере времени необходимо исключить/заменить функции print() и input() 
в анализируемом коде. С ними вы будете замерять время вывода данных 
в терминал и время, потраченное пользователем, на ввод данных, 
а не быстродействие самого алгоритма.
"""

from cProfile import run as profile


def test(meta):
    data = {521: 3733, 1228: 9967, 1229: 9973}

    for k, v in data.items():
        assert v == meta(k)
        print(f'Success: received {v} for {k}')

    print('The tests were successful')


def eratosthenes_sieve(n):
    """Решето Эратосфена"""

    step = 1
    start = 3
    end = 4 * n

    data = [i for i in range(start, end) if i % 2 != 0]
    item = [2]

    if n == 1:
        return 2

    while step < n:

        for i in range(len(data)):

            if data[i] != 0:
                step += 1

                if step == n:
                    return data[i]

                j = i + data[i]

                while j < len(data):
                    data[j] = 0
                    j += data[i]

        item.extend([i for i in data if i != 0])

        start, end = end, end + 2 * n
        data = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(data)):

            for j in item:

                if data[i] % j == 0:
                    data[i] = 0
                    break

# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 18.1 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 739 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 67.7 msec per loop
# 
# Предположительно, алгоритм сложности O(n**2).
# Увеличение количества чисел в 10 раз увеличивает время выполнения приблизительно в 100 раз.
# 
# 
# profile('eratosthenes_sieve(10)')
# 27 function calls in 0.008 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_2.py:45(eratosthenes_sieve)
# 
# profile('eratosthenes_sieve(100)')
# 353 function calls in 0.003 seconds
# 1    0.003    0.003    0.003    0.003 lesson_4__task_2.py:45(eratosthenes_sieve)
# 
# profile('eratosthenes_sieve(1000)')
# 4289 function calls in 0.087 seconds
# 1    0.084    0.084    0.087    0.087 lesson_4__task_2.py:45(eratosthenes_sieve)
# 
# Время выполнения нарастает. Рекурсий нет.


def brute_force(n):
    """Перебор значений"""

    step = 1
    item = 1
    data = [2]

    if n == 1:
        return 2

    while step != n:
        item += 2

        for i in data:
            if item % i == 0:
                break
        else:
            step += 1
            data.append(item)

    return item

# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.brute_force(10)"
# 100 loops, best of 5: 14 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.brute_force(100)"
# 100 loops, best of 5: 942 usec per loop
# 
# python -m timeit -n 100 -s "import lesson_4__task_2" "lesson_4__task_2.brute_force(1000)"
# 100 loops, best of 5: 84.5 msec per loop
# 
# Предположительно, алгоритм сложности O(n**2).
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.
# 
# 
# profile('brute_force(10)')
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4__task_2.py:114(brute_force)
# 
# profile('brute_force(100)')
# 103 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 lesson_4__task_2.py:114(brute_force)
# 
# profile('brute_force(1000)')
# 1003 function calls in 0.130 seconds
# 1    0.129    0.129    0.130    0.130 lesson_4__task_2.py:114(brute_force)
# 
# Время выполнения нарастает. Рекурсий нет.


# ВЫВОД:
# Сложность алгоритмов и время их работы приблизительно одинаковые («Решето Эратосфена» быстрее примерно на 20%).


# test(eratosthenes_sieve)
# test(brute_force)
