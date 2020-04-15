#задача 1
from time import sleep

class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор меняется на 'f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


#задача 2
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * 25 * 0.05


r = Road(20, 5000)
print(r.mass())




#задача 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Vladimir', 'Putin', 'president', 1000000, 500000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())


#задача 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городской машины {self.name} = {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} допустимая'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость служебной машины {self.name} = {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - неполицейская машина'


bmw = SportCar(150, 'черная матовая', 'bmw', False)
huindai = TownCar(70, 'белая', 'huindai', False)
kia = WorkCar(90, 'серая', 'kia', False)
toyota = PoliceCar(120, 'синяя', 'toyota', True)
print(f'Если {toyota.turn_right()}, тогда {kia.stop()}')
print(f'{toyota.name} - полицейская машина? - {toyota.is_police}')
print(f'{toyota.go()} и ее скорость {toyota.show_speed()}')
print(kia.show_speed())
print(f'{huindai.name} - {huindai.color}, {bmw.name} - {bmw.color}')
print(bmw.show_speed())
print(huindai.show_speed())
print(kia.turn_left())
print(kia.show_speed())



#задача 5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас {self.title}. Запуск отрисовки маркером'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
