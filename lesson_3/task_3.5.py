"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def sum_list(input_str):
    input_list = input_str.split()
    sum_str = 0
    for i in input_list:
        try:
            if i == cpec_simv:
                return sum_str, False
            else:
                sum_str += float(i)
        except ValueError:
            continue
    return sum_str, True


cpec_simv = input('Введите специальный символ, который всё остановит: ')
flag = True
final_sum = 0
while flag:
    input_str = input('Введите числа через пробел: ')  # input_str может быть любой переменной, например, a
    promezh_sum, flag = sum_list(input_str)            # тогда input_str = a
    final_sum += promezh_sum
    # print('Сумма: ', final_sum)
    print(f'Сумма: {final_sum:.2f}')                   # 3e5 = 300000, 5e3 =5000
