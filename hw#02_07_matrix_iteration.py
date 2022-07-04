# 7. Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

import random

row_1 = ([random.randint(1, 100) for _ in range(1, 5)])
row_2 = ([random.randint(1, 100) for _ in range(1, 5)])
row_3 = ([random.randint(1, 100) for _ in range(1, 5)])
matrix = [row_1, row_2, row_3]

print('Строки матрицы:')
for element in matrix:
    print(element)

print('Столбцы матрицы:')

for _ in range(0, 4):
    print([element[_] for element in matrix])
