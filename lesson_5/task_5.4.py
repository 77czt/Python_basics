"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('for_5_4.txt') as file_r, open('for_5_4_next.txt', 'w') as file_w:
    for line in file_r.readlines():
        text_num, num_num = line.rstrip().split(' - ')
        file_w.write(f'{numerals[text_num]} - {num_num}\n')
