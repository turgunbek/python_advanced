from abc import ABC, abstractmethod


END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class ComputerColor(ABC):
    """
    Абстрактный класс - для задания #6, содержит методы:
    __repr__,
    __mul__,
    __rmul__
    """

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    """
    Класс цвета, наследуется от абстрактного класса ComputerColor.
    Реализованы методы:
    __repr__,
    __eq__,
    __add__,
    __hash__,
    __mul__,
    __rmul__
    """

    def __init__(self, r=0, g=0, b=0):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            raise ValueError('Colors must be in [0, 255] range!')
        self.r = r
        self.b = b
        self.g = g

    def __repr__(self):
        return f'{START};{self.r};{self.g};{self.b}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other):
        # в случае если значение уровня цвета превысит 255, то полагаем 255
        new_r = min(255, self.r + other.r)
        new_g = min(255, self.g + other.g)
        new_b = min(255, self.b + other.b)

        return Color(new_r, new_g, new_b)

    def __hash__(self):
        return hash(self.__repr__())

    def __mul__(self, c: float):
        if c < 0 or c > 1:
            raise ValueError('c must be in [0, 1]')
        new_r = int(self.r * c)
        new_g = int(self.g * c)
        new_b = int(self.b * c)
        return Color(new_r, new_g, new_b)

    def __rmul__(self, c: float):
        if c < 0 or c > 1:
            raise ValueError('c must be in [0, 1]')
        new_r = int(self.r * c)
        new_g = int(self.g * c)
        new_b = int(self.b * c)
        return Color(new_r, new_g, new_b)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 +
        [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 +
        [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 +
        [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 +
        [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)

    print('Задание #1: вывод цвета')
    print(red)
    print(green)
    print(blue)

    print('\nЗадание #2: сравнение цветов')
    print(red == green)  # Out: False
    print(red == Color(255, 0, 0))  # Out: True

    print('\nЗадание #3: смешивание цветов')
    print(red + green)

    print('\nЗадание #4: уникальные цвета')
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    print('\nЗадание #5: уменьшение контраста')
    print(0.5 * red)
    print(red * 0.5)

    print('\nЗадание #6: HSL - абстрактный класс ComputerColor')
    print_a(red)
