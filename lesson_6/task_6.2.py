"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def square(self):
        return self._length * self._width

    def weight(self, unit, thickness):
        return self.square() * unit * thickness / 1000


weight_unit = Road(25, 0.05)
# print(f'Масса асфальта 1 кв.м {weight_unit.weight()} кг')
length = float(input('Длина дороги (м): '))
width = float(input('Ширина дороги (м): '))
result_sq = Road(length, width)
# print(f'Площадь дороги {result_sq.square()} кв.м')
print(f'Масса асфальта для дороги площадью {result_sq.square()} кв.м {result_sq.weight(25, 5)} т.')
