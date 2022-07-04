# 3. Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

import random

my_tuple = tuple([round(random.randint(1, 5)/random.randint(5, 10), 2) for _ in range(10)])
print(f"Here's the tuple: {my_tuple}")
print(f"Max value is {max(my_tuple)}, and min value is {min(my_tuple)}")
