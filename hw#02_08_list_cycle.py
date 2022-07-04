# 8. Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

import random

# Генерирую список случайных чисел случайной длины (от 5 до 10 элементов)
my_list = [random.randint(5, 100) for _ in range(0, random.randint(5, 10))]

print(f'Сгенерирован список: {my_list}')
for _ in range(0, len(my_list)):
    print(f'Объект {my_list[_]} с индексом {_}')
