"""
5.  Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.

    Подсказка: использовать функцию reduce().
"""
from functools import reduce

my_spis = [i for i in range(100, 1001) if i % 2 == 0]
print(my_spis)
my_fuct = lambda a, b: a*b
product = reduce(my_fuct, my_spis)
print(product)