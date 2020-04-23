"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны 
каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

a = tuple(range(2, 100))
b = tuple(range(2, 10))
c = [0 for _ in range(len(b))]

for i in range(len(a)):

    for j in range(len(b)):

        if a[i] % b[j] == 0:
            c[j] += 1

for i in range(len(b)):
    print(f'{b[i]}: {c[i]}')
