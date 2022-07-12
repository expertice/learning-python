"""*ЗАДАЧА 1:
Реализовать класс Person, у которого должно быть два публичных поля: age и name.
Также у него должен быть следующий набор методов: know(person), который позволяет
добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека"""


class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.friends = []

    def know(self, person):
        if self.is_known(person):
            print("They're friends already")
        else:
            self.friends.append(person)

    def is_known(self, person):
        if person in self.friends:
            return True
        else:
            return False


p1 = Person(7, 'Ivan')
p2 = Person(8, 'Lena')
p3 = Person(7, 'Dima')

p1.know(p2.name)
p1.know(p3.name)
print(p1.friends)
p1.know(p2.name)

