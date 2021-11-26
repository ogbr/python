class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self):
        # name = input("Введите имя: ")
        # surname = input("Введите фамилию: ")
        # position = input("Введите должность: ")
        # _income={"wage":float(list(input("Введите оклад: "))), "bonus": float(list(input("Введите премию: ")))}

        self.name = "Ольга"
        self.surname = "Юльметова"
        self.position = "начальник"
        self._income = {"wage": 100, "bonus": 50}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


a = Position()
a.get_full_name()
a.get_total_income()
