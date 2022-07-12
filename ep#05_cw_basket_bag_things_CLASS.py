"""*ЗАДАЧА 1:
1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
В объекты класса корзина можно помещать разные объекты;
2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
4. Если вместимости недостаточно, сказать, что объект поместить нельзя."""


class HandBox(object):
    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('This HandBox size = {}'.format(self.size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} is in a HandBox'.format(smth))
        else:
            print('{} is to big for a HandBox with size = {}'.format(smth, self.size))


class Bag(HandBox):
    def get_size(self):
        print('This Bag size = {}'.format(self.size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} is in a Bag'.format(smth))
        else:
            print('{} is to big for a Bag with size = {}'.format(smth, self.size))


class Thing(object):
    def __init__(self, size):
        self.size = size


box1 = HandBox(20)
box1.get_size()

bag1 = Bag(123)
bag1.get_size()

smth1 = Thing(10)
smth2 = Thing(30)
smth3 = Thing(130)

box1.put_smth(smth1)
box1.put_smth(smth2)

bag1.put_smth(smth2)
bag1.put_smth(smth3)