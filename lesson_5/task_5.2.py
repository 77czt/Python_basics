"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('text_user.txt') as file_5_2:
    text_user = file_5_2.readlines()

i = 1
for el in text_user:
    print(el, end='')
    print(f'Количество слов в строке {i}: {el.count(" ") + 1}')
    i += 1
print(f'Всего строк: {len(text_user)}')
