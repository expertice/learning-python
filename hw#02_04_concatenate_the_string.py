# 4. Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'

my_list = ['Earth', 'Russia', 'Moscow']

for _ in range(0, len(my_list) - 1):
    my_list[_] += ' ->'

# слияние в одну строку с разделителем ' ' при помощи join
# результат выражения можно присвоить переменной
# my_string = ' '.join(my_list)
print(' '.join(my_list))

# вывод в развернутом виде
# результат выражения нельзя присвоить переменной
print(*my_list)
