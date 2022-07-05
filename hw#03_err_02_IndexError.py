# 2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть.
#     Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так

import random


def list_generator():
    my_list = []
    for _ in range(0, random.randint(5, 10)):
        my_list.append(random.randint(-100, 00))
    return my_list


my_fresh_list = list_generator()
print(f"List: {my_fresh_list}")
promt = input('Enter an index of element you want to see: ')
try:
    print(my_fresh_list[int(promt)])
except IndexError:
    print("There's no element with this index (IndexError)")
except ValueError:
    print("Index must be a figure (ValueError)")
except Exception as e:
    print("Error! ", e)
