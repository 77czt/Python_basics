"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name_script, name, norma, stavka, bonus = argv
zp_name = f'Имя: {name}. ЗП: {int(norma) * int(stavka) + int(bonus)} рублей '

print(zp_name)