"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина марки {self.name} цвет {self.color} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'Машина марки {self.name} цвета {self.color} остановилась')

    def turn(self, direction):
        if direction == '':
            print(f'Машина марки {self.name} цвета {self.color} едет прямо')
        else:
            print(f'Машина марки {self.name} цвета {self.color} повернула на{direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print(f'Превышение на {self.speed - 60} км/ч')

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 40:
            print(f'Превышение на {self.speed - 40} км/ч')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name,):
        Car.__init__(self, speed, color, name, is_police=True)

town_car_1 = TownCar(76, 'черный', 'Lincoln')
town_car_1.go()
town_car_1.stop()
town_car_1.turn('')
town_car_1.show_speed()

sport_car_1 = SportCar(210, 'синий', 'Skyline')
sport_car_1.go()
sport_car_1.stop()
sport_car_1.turn('лево')
sport_car_1.show_speed()

work_car_1 = WorkCar(60, 'зеленый', 'ЗиЛ')
work_car_1.go()
work_car_1.stop()
work_car_1.turn('лево')
work_car_1.show_speed()

police_car_1 = PoliceCar(90, 'белый', 'Лада')
police_car_1.go()
police_car_1.stop()
police_car_1.turn('лево')
police_car_1.show_speed()
