import math
from idlelib.pyshell import fix_x11_paste


class Figure:
    sides_count = 0

    def __init__(self, __sides: tuple | list | int, __color: tuple | list | int, filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

        if isinstance(__sides, (list, tuple)) and len(__sides) != self.sides_count:
            sides_size = [1] * self.sides_count
        elif isinstance(__sides, int) and self.sides_count == 1:
            sides_size = [__sides]
        else:
            sides_size = __sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):  # добавить "__"
        if all(0 <= value < 256 for value in (r, g, b)):
            return True
        else:
            print('Ошибка значения цвета')

    def set_color(self, r, g, b):
        if all(isinstance(value, int) for value in (r, g, b)):
            if self.__is_valid_color(r, g, b) is True:
                self.__color = (r, g, b)
                return self.__color
            else:
                print('Ошибка значения цвета. Изменение цвета невозможно')

    def __is_valid_sides(self, *args):  # добавить "__"
        if len(args) == len(self.__sides):
            for side in args:
                if isinstance(side, int) and side > 0:
                    return True
                else:
                    return False
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        sides = self.__sides if isinstance(self.__sides, (list, tuple)) else [self.__sides]
        perimeter = sum(sides)
        return perimeter

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides: tuple | list, __color: tuple | list):
        super().__init__(__sides, __color)

        if isinstance(__sides, list) and len(__sides) == 1:
            for side in __sides:
                self.__radius = side / 2 * math.pi
        elif isinstance(__sides, int):
            self.__radius = __sides / 2 * math.pi
        else:
            print('У круга не может быть больше одной стороны')

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color):
        super().__init__(__sides, __color)

        if len(__sides) != 3:
            print('У треугольника должно быть три стороны')

    def get_square(self):
        return super().__len__() / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides, __color):
        super().__init__(__sides, __color)
        self.__sides = [__sides[0]] * self.sides_count

    def get_volume(self):
        volume = self.__sides[0] ** 3
        return volume


# Проверка Figure
figure = Figure((2, 5, 9), (278, 222, 222))
print(figure.get_color())
figure._Figure__is_valid_color(973, 489, 979)
figure.set_color(0, 0, 1)
print(figure._Figure__is_valid_sides('dff'))
figure.get_sides()

circle1 = Circle(10, (200, 200, 100))  # (Цвет, стороны)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

# Проверка на площадь и объем:
triangle = Triangle((2, 3, 5), (1, 3, 4))
print(triangle.get_square())
cube1 = Cube((9, 300, 100), (10, 0, 0))
print(cube1.get_volume())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 1, 1, 1, 1, 1, 9, 8, 8, 8)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))