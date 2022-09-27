"""Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль:
ИМЯ_ФУНКЦИИ is canceled!"""


def cancel_it(func):
    def make_stop(*args):
        print(f"{func.__name__} IS CANCELLED")
    return make_stop


@cancel_it
def sum_some(*args):
    result = 0
    for arg in args:
        result += arg
    print(f"result is {result}")
    return result


if __name__ == '__main__':
    sum_some(1, 2, 3, 5, 7, 8)