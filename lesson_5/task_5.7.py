"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

with open('firmes.txt') as file:
    firmes = file.readlines()

profit_losses = 0
profit = 0
counter = 0
av_profit = 0
result_dict = {}
for line in firmes:
    data = line.split()
    profit_losses = (int(data[2]) - int(data[3]))
    if int(data[2]) - int(data[3]) > 0:
        counter += 1
        profit += profit_losses
    result_dict.setdefault(data[0], profit_losses)
av_profit += float(profit / counter)
result_dict.setdefault('average_profit', av_profit)

with open('result_dict_j.json', 'w') as result_j_5_7:
    json.dump(result_dict, result_j_5_7)

with open('result_dict_j.json') as result_j_5_7:
    result_j_5_7_json = json.load(result_j_5_7)

print(result_j_5_7_json)

# print(f'Прибыль всех фирм = {profit} $')
# print(f'Средняя прибыль фирм = {av_profit} $')
# print(result_dict)
