"""1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
text_user = input('Введите первую строку: ')
with open('text_user.txt', 'w') as file_5_1:
    while text_user:
        file_5_1.write(text_user+'\n')
        text_user = input('Введите следующую строку: ')
