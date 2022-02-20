"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
from random import randint

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_line = ''
        for line in self.matrix:
            for el in line:
                matrix_line += f'{el:4}'
            matrix_line += '\n'
        return matrix_line

    def __add__(self, other):
        matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        return Matrix(matrix)

m_1 = Matrix([[randint(-5, 10) for a in range(5)] for b in range(4)])
m_2 = Matrix([[randint(-5, 10) for a in range(5)] for b in range(4)])
m_sum = m_1 + m_2
print(m_1)
print(m_2)
print(m_sum)
