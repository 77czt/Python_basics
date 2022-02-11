"""
6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
with open('subjects.txt') as file_5_6:
    my_subjects = file_5_6.readlines()
    # for i in my_subjects:
    #     print(i, end='')

my_subjects_dict = {}
for line in my_subjects:
    subject_single = line.split()
    # print(subject_single)
    sum_single = 0
    for el in subject_single[1:]:
        num_single = ''
        for i in el:
            if i.isdigit():
                num_single += i
        # print(num_single)
        sum_single += int(num_single)
    # print(sum_single)
    my_subjects_dict.setdefault(subject_single[0], sum_single)
print(my_subjects_dict)
