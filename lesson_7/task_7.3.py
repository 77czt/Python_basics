"""3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где
количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд
записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15,
количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****. """
class Cell:
    def __init__(self, cell_cell):
        self.cell_cell = cell_cell

    def __add__(self, other):
        cell = self.cell_cell + other.cell_cell
        return Cell(cell)

    def __sub__(self, other):
        if self.cell_cell > other.cell_cell:
            cell = self.cell_cell - other.cell_cell
            return Cell(cell)
        else:
            print('Вычитание невозможно: дочерняя клетка больше материнской')
            cell = 0
            return Cell(cell)

    def __mul__(self, other):
        cell = self.cell_cell * other.cell_cell
        return cell

    def __truediv__(self, other):
        cell = self.cell_cell // other.cell_cell
        return cell

    def make_order(self, arg):
            if type(self.cell_cell) is not None:
                star_line = (('*' * arg) + '\n') * (self.cell_cell // arg) + ('*' * (self.cell_cell % arg))
                return star_line

cell_cell_1 = 9
cell_cell_2 = 7
arg_1 = int(input('Кол-во ячеек в ряду материнской клетки = '))
arg_2 = int(input('Кол-во ячеек в ряду дочерней клетки = '))
arg_total = int(input('Кол-во ячеек в ряду реконструированной клетки клетки = '))
print(f'Материнская клетка({cell_cell_1})\n{(Cell(cell_cell_1).make_order(arg_1))}')
print(f'Дочерняя клетка({cell_cell_2})\n{(Cell(cell_cell_2).make_order(arg_2))}')
total_add = Cell(cell_cell_2) + Cell(cell_cell_1)
c1_add_c2 = cell_cell_1 + cell_cell_2
print(f'Реконструированная клетка СЛОЖЕНИЕ ({c1_add_c2})\n{total_add.make_order(arg_total)}')
total_sub = Cell(cell_cell_1) - Cell(cell_cell_2)
c1_sub_c2 = cell_cell_1 - cell_cell_2
print(f'Реконструированная клетка ВЫЧИТАНИЕ ({c1_sub_c2})\n{total_sub.make_order(arg_total)}')
total_mul = Cell(cell_cell_1 * cell_cell_2)
c1_mul_c2 = cell_cell_2 * cell_cell_1
print(f'Реконструированная клетка УМНОЖЕНИЕ ({c1_mul_c2})\n{total_mul.make_order(arg_total)}')
total_truediv = Cell(cell_cell_1 // cell_cell_2)
c1_div_c2 = cell_cell_1 // cell_cell_2
print(f'Реконструированная клетка ДЕЛЕНИЕ ({c1_div_c2})\n{total_truediv.make_order(arg_total)}')
