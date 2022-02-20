"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def material(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def material(self):
        fabric_coat = self.v/6.5 + 0.5
        return round(fabric_coat, 2)

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def material(self):
        fabric_suit = (2*self.h)/100 + 0.3
        return round(fabric_suit, 2)

coat_1 = Coat(int(input('Размер пальто: ')))
print(f'Расход ткани на пальто {coat_1.material} кв.м')
suit_1 = Suit(float(input('Рост в см: ')))
print((f'Расход ткани на костюм {suit_1.material} кв.м '))
print(f'Общий расход ткани {coat_1.material + suit_1.material} кв.м')
