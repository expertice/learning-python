# ЗАДАЧА 3
#
# Написать класс Animal и Human,
# сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ
class Animal(object):

    def __init__(self, name, aggressive):
        self.name = name
        self.aggressive = aggressive


    def attack_human(self, human):
        if self.aggressive and not human.aggressive:
            print('Атака {} на {} прошла успешно!'.format(self.name, human.name))
            human.dangerous_animals.append(self)
        else:
            print('Атака {} на {} не удалась!'.format(self.name, human.name))

class Human(Animal):

    def __init__(self, name, aggressive):
        self.name = name
        self.dangerous_animals = []
        self.aggressive = aggressive

    def is_dangerous(self, animal):
        answers = {True : 'ДА', False : 'НЕТ'}
        return answers[animal in self.dangerous_animals]



def main():
    """Основная функция"""

    print('\n\n')
    hercules = Human('Геракл', True)
    prometeus = Human('Прометей', False)

    hydra = Animal('Гидра', True)
    hawk = Animal('Ястреб', True)
    lamb = Animal('Овца', False)
    print('\nПолучение людьми опыта общения с животными:\n ')
    hydra.attack_human(hercules)
    hawk.attack_human(hercules)
    lamb.attack_human(hercules)

    hydra.attack_human(prometeus)
    hawk.attack_human(prometeus)
    lamb.attack_human(prometeus)

    print('\nПолучение людьми опыта общения с другими людьми:\n ')
    hercules.attack_human(prometeus)

    print('\nПроверка накопленного людьми опыта общения с животными:\n ')
    print('Опасна ли {} для {}? : {}'.format(hydra.name, hercules.name, hercules.is_dangerous(hydra)))
    print('Опасен ли {} для {}? : {}'.format(hawk.name, hercules.name, hercules.is_dangerous(hawk)))
    print('Опасна ли {} для {}? : {}'.format(lamb.name, hercules.name, hercules.is_dangerous(lamb)))

    print('Опасна ли {} для {}? : {}'.format(hydra.name, prometeus.name, prometeus.is_dangerous(hydra)))
    print('Опасен ли {} для {}? : {}'.format(hawk.name, prometeus.name, prometeus.is_dangerous(hawk)))
    print('Опасна ли {} для {}? : {}'.format(lamb.name, prometeus.name, prometeus.is_dangerous(lamb)))

    print('\nПроверка накопленного людьми опыта общения с другими людьми:\n ')
    print('Опасен ли {} для {}? : {}'.format(hercules.name, prometeus.name, prometeus.is_dangerous(hercules)))


if __name__ == '__main__':
    main()