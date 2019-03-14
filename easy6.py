# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:
    def __init__(self, speed, side, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.side = int(side)
        self.name = name
        self.is_police = bool(is_police)
        self.go()
        self.stop()
        self.parameters()
        self.turn(side)

    def go(self):
        if self.speed != 0:
            print('Машина едет со скоростью', self.speed, "км/ч")

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, side):
        if side == 1:
            print('Машина поворачивает влево')
        elif side == 2:
            print('Машина поворачивает направо')
        elif side == 0:
            print('Машина стоит на месте')

    def parameters(self):
        print(self.color, self.name)
        if self.is_police == True:
            print("Машина работает в полиции")
        else:
            print("Машина не работает в полиции")


class SportCar(TownCar):
    pass


class WorkCar(TownCar):
    pass


class PoliceCar(TownCar):
    pass


town_car = TownCar(150, 1, "черный", "Logan", "")
print("*"*40)
sport_car = SportCar(250, 2, "красный", "Ferrari", "")
print("*"*40)
work_car = WorkCar(0, 0, "Синий", "KAMAZ", "")
print("*"*40)
police_car = PoliceCar(80, 2, "сине-белый", "UAZ", "1")
