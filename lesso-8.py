"""задача 1"""


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Дата указана верно!'
                else:
                    return f'Неправильный год!'
            else:
                return f'Неправильный месяц!'
        else:
            return f'Неправильный день!'

    def __str__(self):
        return f'Сегодня - {Date.extract(self.date)}'


Today = Date('21 - 4 - 2020')
print(Today)
print(Date.valid(1, 1, 2030))
print(Today.valid(1, 13, 2019))
print(Date.valid(1, 11, 2000))
print(Date.extract('11 - 11 - 2011'))
print(Today.extract('11 - 11 - 2020'))


"""задача 2"""
class DivisionNull:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def solution(a, b):
        try:
            return (a / b)
        except:
            return (f"Делить на ноль нельзя!")


D = DivisionNull(10, 100)
print(D.solution(100, 0))
print(DivisionNull.solution(10, 0))
print(DivisionNull.solution(10, 5))

"""задача 3"""

class Error:
    def __init__(self, *args):
        self.my_list = []

    def input(self):
        while True:
            try:
                a = int(input('Введите значение и нажмите Enter - '))
                self.my_list.append(a)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                c = input(f'Попробовать еще раз? Y/N')

                if c == 'Y' or c == 'y':
                    print(try_except.input())
                elif c == 'N' or c == 'n':
                    return f'Конец'
                else:
                    return f'Конец'

try_except = Error(1)
print(try_except.input())




"""задача 6"""

class StoreMashines:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.to_my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Устройство - {self.name}, цена - {self.price}, количество - {self.quantity}'

    def reception(self):
        try:
            n = input(f'Введите наименование: ')
            p = int(input(f'Введите цену за единицу: '))
            q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': n, 'Цена': p, 'Количество': q}
            self.my_unit.update(unique)
            self.to_my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.to_my_store}')
        except:
            return f'Ошибка ввода!'

        print(f'Для выхода - s, для продолжения - Enter')
        s = input(f'-> ')
        if s == 'S' or s == 's':
            self.my_store_full.append(self.to_my_store)
            print(f'Склад: \n {self.my_store_full}')
            return f'Конец'
        else:
            return StoreMashines.reception(self)

u_1 = StoreMashines('HP', 10000, 5, 10)
print(u_1.reception())



"""задача 7"""

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, с):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + с.a} + ({self.b + с.b}) * i'

    def __mul__(self, с):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * с.a - (self.b * с.b)} + ({self.b * с.a + self.a * с.b}) * i'

    def __str__(self):
        return f'z = {self.a} + ({self.b}) * i'


z_1 = ComplexNumber(1, - 2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)