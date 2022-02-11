"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
# V.1 list
while True:
    try:
        m = int(input('Введите порядковый номер месяца года: '))
        if m < 1 or m > 12:
            raise ValueError
    except ValueError:
            print('Должно быть целое число от 1 до 12! ')  #, end=" ")
    else:
        if m in [12, 1, 2]:
            print('Зима')
        elif m in [3, 4, 5]:
            print('Весна')
        elif m in [6, 7, 8]:
            print('Лето')
        elif m in [9, 10, 11]:
            print('Осень')
        break

# V.2 Dict
year = {}
year = year.fromkeys([12, 1, 2], 'Зима')
year.update({}.fromkeys([3, 4, 5], 'Весна'))
year.update({}.fromkeys([6, 7, 8], 'Лето'))
year.update({}.fromkeys([9, 10, 11], 'Осень'))
# year = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
#         9: 'Осень', 10: 'Осень', 11: 'Осень'}
while True:
    try:
        m = int(input('Введите порядковый номер месяца года: '))
        if m < 1 or m > 12:
            raise ValueError
    except ValueError:
        print('Должно быть целое число от 1 до 12! ')
    else:
        for month_number, season in year.items():
            if m == month_number:
                print(season)
        break
