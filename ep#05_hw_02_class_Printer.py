"""*ЗАДАЧА 2:
Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *"""


class Printer(object):
    def __init__(self):
        self.queue = []
        print("Created new Printer object")

    def log(self, *values):
        self.queue = list(values)  # [value for value in values]
        print(*self.queue)


class FormattedPrinter(Printer):
    def __init__(self, *values):
        print('\n************')
        self.log(*values)
        print('************')


p1 = Printer()
p1.log(1, 2, 3, 4)

p2 = FormattedPrinter(3, 4, 5, 6)
