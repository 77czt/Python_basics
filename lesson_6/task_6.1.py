"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from itertools import cycle
import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self, color=False):
        if color:
            result = f'Горит {self.__color}'
            return result


red = TrafficLight('Red')
yellow = TrafficLight('Yellow')
green = TrafficLight('Green')
trflight = [red.running(True), yellow.running(True), green.running(True)]
for light in cycle(trflight):
    print(light)
    if light == red.running(True):
        time.sleep(7)
    elif light == yellow.running(True):
        time.sleep(2)
    elif light == green.running(True):
        time.sleep(4)
