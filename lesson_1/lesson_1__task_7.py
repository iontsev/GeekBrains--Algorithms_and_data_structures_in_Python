"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""

i = int(input("Год: "))

if i % 4 != 0 or (i % 100 == 0 and i % 400 != 0):
    print("Обычный")
else:
    print("Високосный")
