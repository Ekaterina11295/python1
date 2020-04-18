# задача 1
class Matrix:
    def __init__(self, m_1, m_2):
        self.m_1 = m_1
        self.m_2 = m_2

    def __add__(self):
        m = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

        for i in range(len(self.m_1)):

            for j in range(len(self.m_2[i])):
                m[i][j] = self.m_1[i][j] + self.m_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


matrix = Matrix([[31, 22, 0],[37, 43, 0],[51, 86, 0]],[[3, 5, 32],[2, 4, 6],[-1, 64, -8]])
print(matrix.__add__())

#задача 2
class Cloth:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_c1(self):
        return round(self.v / 6.5 + 0.5)

    def get_square_c2(self):
        return round(self.h * 2 + 0.3)

    @property
    def get_sq_full(self):
        return str(f'Общая площадь необходимой ткани = {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3))}')


class Coat(Cloth):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c1 = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто = {self.square_c1}'


class Costume(Cloth):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c2 = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм = {self.square_c2}'


coat = Coat(5, 6)
costume = Costume(3, 2)
print(coat)
print(costume)
print(coat.get_sq_full)
print(costume.get_sq_full)

#задача 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции - {self.quantity * "*"}'

    def __add__(self, other):  #  сложение
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):  #  вычитание
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print('Отрицательное число!')

    def __mul__(self, other):  #  умножение
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):  #  деление
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(12)
cells2 = Cell(15)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2 / cells1)
print(cells1 * cells2)
print(cells2.make_order(5))
print(cells1.make_order(5))