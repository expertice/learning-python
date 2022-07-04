# 9. Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

my_list = ['resurrect', 'to-delete', 'resolve', 'to-delete', 'confirm', 'granted', 'to-delete']

for element in range(len(my_list) - 1, -1, -1):  # идём от конца к началу
    print(element, my_list[element])
    if my_list[element] == 'to-delete':
        my_list.pop(element)

print(my_list)
