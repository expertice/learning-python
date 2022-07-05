# 1. Написать функцию, которая принимает на вход два аргумента.
#     Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность.
#     Если знаки разные - возвращаем 0


def calc(a, b):
    result = 0
    if a > 0 and b > 0:
        result = a + b
    elif a < 0 and b < 0:
        result = a - b
    return result


case1 = calc(2, 3)
case2 = calc(-1, -5)
case3 = calc(-2, 5)
print(case1, case2, case3)
