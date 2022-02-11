"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint

base_list = []
num = 15
counter = 1
n = int
a = int(input('Введите значение первого элемента : '))
b = int(input('Введите значение последнего элемента: '))
while counter <= num:
    n = randint(a, b)
    base_list.append(n)
    counter += 1
print(base_list)

# result_list = []
# for i in range(1, len(base_list)-1):
#     if base_list[i] < base_list[(i+1)]:
#         result_list.append(base_list[i+1])
result_list = [base_list[i+1] for i in range(1, len(base_list)-1) if base_list[i] < base_list[(i+1)]]
print(result_list)