class Cell:
    __CellAmount = 0

    def __init__(self, n):
        self.__CellAmount = n

    def __add__(self, second_cell):
        return self.__CellAmount + second_cell.__CellAmount

    def __sub__(self, second_cell):
        return abs(self.__CellAmount - second_cell.__CellAmount)

    def __mul__(self, second_cell):
        return self.__CellAmount * second_cell.__CellAmount

    def __truediv__(self, second_cell):
        return round(self.__CellAmount / second_cell.__CellAmount, 2)

    def __str__(self):
        return str(self.__CellAmount)

    def make_order(self, num):
        n = self.__CellAmount
        x = n // num
        d = ('*' * num + '\n') * x + '*' * (n - x * num)
        print(d)


c_1 = Cell(10)
c_2 = Cell(7)
print(f"Результат сложения клеток: {c_1 + c_2}")
print(f"Результат вычитания клеток: {c_1 - c_2}")
print(f"Результат умножения клеток: {c_1 * c_2}")
print(f"Результат деления клеток: {c_1 / c_2}")
# число клеток в ряду
k = 5
print(f"Вывод в * при общем числе клеток {c_1} и числе клеток в ряду {k} :")
c_1.make_order(k)
print(f"Вывод в * при общем числе клеток {c_2} и числе клеток в ряду {k} :")
c_2.make_order(k)
