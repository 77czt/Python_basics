"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""
def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    return sum(my_list[-2:])


print(my_func(int(input('Число_1 = ')), int(input('Число_2 = ')), int(input('Число_3 = '))))
