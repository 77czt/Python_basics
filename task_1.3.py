"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input("Введите любое целое число ")
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
summa = n + nn + nnn
print(summa)

n = input("Введите любое целое число ")
nn = n + n
nnn = n + n + n
summa = int(n) + int(nn) + int(nnn)
print(summa)
