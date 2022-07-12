"""*ЗАДАЧА 3:
Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)

Слегка дополнил задачу:
Человек наследуется от животного.
И у животных и у людей добавлен параметр агрессии.
У животного и у человека есть метод Атаковать человека.
Если параметр агрессии у нападающего и жертвы совпадает считается, что жертва отбилась и не считает нападавшего опасным.
В противном случае жертва добавляет нападающего в перечень опасных для себя существ
"""


class Animal(object):

    def __init__(self, individual, agression_level):
        self.dang_list = []
        self.individual = individual
        self.agression_level = agression_level

    def attack_human(self, enemy_type,enemy_level):
        if enemy_level > self.agression_level:
            self.dang_list.append(enemy_type)

    def get_dang_list(self):
        print(self.dang_list)


class Human(Animal):
    def is_dangerous(self, enemy_type, enemy_level):
        if enemy_type in self.dang_list:
            return True
        elif enemy_level > self.agression_level:
            return True
        else:
            return False


h1 = Human('Ivan', 100)
h2 = Human('Papakot', 250)
h1.get_dang_list()
h1.attack_human(h2.individual, h2.agression_level)
h1.get_dang_list()
a1 = Animal('Snake', 120)
h2.attack_human(a1.individual, a1.agression_level)
h2.get_dang_list()
