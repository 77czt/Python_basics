"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
with open('payment.txt', 'w') as file_for_5_3:
    file_for_5_3.writelines('Ronaldo 120000.99\n'
                            'Messi 115000.99\n'
                            'Ryzhykov 999.99\n'
                            'Maradona 24999.99\n'
                            'Dzuba 19999.99\n'
                            'Bystrov 9999.99\n'
                            'Samedov 5000\n'
                            'Ibragimovich 58999.99\n'
                            'Kerimov 3250\n'
                            'Belousov 1999.99\n'
                            'Салибеков 8686')
with open('payment.txt') as file_for_5_3:
    payments = file_for_5_3.readlines()

sum_pay = 0
losers = []
for el in payments:
    name, payment = el.split()
    if float(payment) <= 20000:
        losers.append(name)
        # print(name)
    sum_pay += float(payment)
avg_pay = sum_pay/len(payments)
print(f'Средняя З/П сотрудников: {avg_pay:.2f}')
print('Сотрудники с З/П менее 20000: '+", ".join(losers))
