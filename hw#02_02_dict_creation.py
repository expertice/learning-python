# 2. Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

import random
my_dict = {}

for i in range(0, 5):
    element = random.randint(0, 100)
    my_dict.update({element: str(element)})

# первый вариант обхода
for key in my_dict:
    print(key, type(key), ' :', my_dict[key], type(my_dict[key]))

# второй вариант обхода
for key, value in my_dict.items():
    print(key, ' -> ', value)
