""" *ЗАДАЧА 2:
Пользователь вводит список чисел через пробел. если ввел:
1 число, строим квадрат
2 числа, строим прямоугольник
3 числа, треугольник
4 числа, многоугольник

вычисляем периметр и площадь. выводим в консоль.
можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами. """


class Square(object):
    def __init__(self, *sides):
        self.sides = sides

    def calculate_area(self):
        self.area =


class Rectangle(Square):
    pass


class Triangle(Square):
    pass


class Polygon(Square):
    pass


class Figure(object):
    def __init__(self, sides):
        self.sides = sides

    def is_input_correct(self):
        if len(self.sides) > 4:
            return False
        return True

    def convert_values(self):
        self.sides = self.sides.split(' ')
        for element in self.sides:
            self.sides[element] = int(self.sides[element])

    def square_calc(self):
        square = 1
        if not self.is_input_correct():
            print(square)
            return square


p = input("Enter the length of the sides separated by a space: ")
fig1 = Figure(p)
try:
    fig1.convert_values()
    print("Square counting")
except Exception as e:
    print("Can't convert to numerical values")
