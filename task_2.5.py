"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""
rrr = [999, 345, 55, 55, 55, 9, 9, 6, 3, 2, -2]
print(rrr)
rrr.sort(reverse=True)
while True:
    try:
        n = int(input('Введите новый элемент целым числом: '))
    except ValueError:
        print('Введите целое число')
    else:
        i = 0
        while i < len(rrr):
            if n == rrr[i]:
                rrr.insert((rrr.index(n) + rrr.count(n)), n)
                # print(rrr.index(n))
                break
            elif n > rrr[i]:
                rrr.insert(rrr.index(rrr[i]), n)
                # print(rrr.index(n))
                break
            elif n < rrr[-1]:
                rrr.append(n)
                # print(rrr.index(n))
                break
            i += 1
        print(rrr)