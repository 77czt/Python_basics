"""
Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются соседние элементы 0 и 1, 2 и 3 и т.д.
При нечетном значении элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию Input().
"""
list = input('Введите любые значения через пробел: ')
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list.split()
print(list)
# V.1
i = 0
while i < (len(list)-1):
    (list[i], list[i+1]) = (list[i+1], list[i])
    i += 2
print(list)