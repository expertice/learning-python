# 1. Создать лист из 6 любых чисел. Отсортировать его по возрастанию

import random

my_list = []

for i in range(0, 6):
    my_list.append(random.randint(1, 100))

print(my_list)
print(sorted(my_list))
