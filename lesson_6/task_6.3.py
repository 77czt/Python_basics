"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        result_p = f'{self.name} {self.surname}'
        return result_p

    def get_total_income(self):
        result_inc = self._income['wage'] + self._income['bonus']
        return result_inc

    def position_out(self):
        result_pos_out = self.position
        return result_pos_out


position_1 = Position('Bill', 'Gates', 'businessman', 9999, 888)
print(f"{position_1.get_full_name()}'s total income as a {position_1.position_out()} is ${position_1.get_total_income()}.")
