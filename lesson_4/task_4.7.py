"""
7.  Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
    for el in fact(n).
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
    начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce
from itertools import count
from math import factorial

def fact(n):
    fact_n = 1
    for i in count(fact_n):
        if i <= n:
            print(f'{i}!:', end=' ')
            # result = factorial(i)
            result = reduce(lambda a, b: a*b, range(1, i+1))
            yield result
        else:
            break

n = int(input('Введите число для, из которого вывести факториал = '))
for el in fact(n):
    pass
    print(el)
