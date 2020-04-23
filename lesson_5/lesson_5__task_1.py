"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль 
за четыре квартала для каждого предприятия. Программа должна определить 
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования 
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple


Enterprise = namedtuple('Enterprise', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

enterprise_count = int(input('Введите количество предприятий для анализа: '))
enterprises = [0 for _ in range(enterprise_count)]
profit_sum = 0

for i in range(enterprise_count):
    name = input(f'Введите название {i+1}-го предприятия: ')
    quarters = [float(input(f'Введите прибыль в {i}-ом квартале: ')) for i in range(4)]
    year = 0

    for quarter in quarters:
        year += quarter

    profit_sum += year
    enterprises[i] = Enterprise(name, *quarters, year)

if enterprise_count == 1:
    print(f'Для анализа передано только одно предприятие: {enterprises[0].name}. Eго годовая прибыль: {enterprises[0].year}')
else:
    profit_average = profit_sum / enterprise_count
    less = []
    more = []

    for i in range(enterprise_count):

        if enterprises[i].year < profit_average:
            less.append(enterprises[i])
        elif enterprises[i].year > profit_average:
            more.append(enterprises[i])

    print(f'\nСредняя годовая прибыль по предприятиям: {profit_average: .2f}')
    print(f'\nПредприятия, чья прибыль выше средней:')

    for item in more:
        print(f'{item.name} ({item.year: .2f})')

    print(f'\nПредприятия, чья прибыль ниже средней:')

    for item in less:
        print(f'{item.name} ({item.year: .2f})')
