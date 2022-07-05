# Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль


def comparator(a, b, c):
    result = [a, b, c]
    #  result.index(min(result)) - индекс наименьшего элемента
    result.pop(result.index(min(result)))  # удаляем наименьший элемент по индексу
    print(result)


comparator(2, 7, 18)
