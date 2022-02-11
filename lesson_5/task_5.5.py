"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

with open('for_5_5.txt', 'w') as file:
    for i in range(10):
        file.write(f'{randint(-5, 10)} ')

with open('for_5_5.txt') as file:
    nums_in_list = file.read().split()
    sum_el = 0
    for el in nums_in_list:
        sum_el += int(el)
print(f'Сумма чисел ({" ".join(nums_in_list)}): {sum_el}')
