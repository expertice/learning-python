# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
#     Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру,
#     иначе - к нижнему


def converter(string, case=True):
    if case:
        result = string.upper()
    else:
        result = string.lower()
    print(result)
    return result


converter('AbRaCaDaBrA')
converter('AbRaCaDaBrA', False)
