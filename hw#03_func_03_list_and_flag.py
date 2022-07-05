# Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг.
#     Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
#     если флаг отрицателен - возвращаем новый список с четными числами из входного списка
import random


def evenodd(func_list, flag):
    result = []
    _ = 0
    if not flag:
        _ = 1
    print(f"Flag is {flag}, List is {func_list}")
    for i in range(0, len(func_list)):
        if func_list[i] % 2 != _:
            result.append(func_list[i])
    print(result)


my_list = []
for _ in range(0, random.randint(5, 10)):
    my_list.append(random.randint(-100, 00))

evenodd(my_list, random.randint(0, 1))
