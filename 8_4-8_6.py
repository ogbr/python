from abc import ABC, abstractmethod


class WarehouseValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

    def __str__(self):
        return super().__str__() + " - " + self.errors


class Warehouse:
    department = {'managers': {'printer': [], 'scanner': [], 'xerox': []},
                  'analytics': {'printer': [], 'scanner': [], 'xerox': []}}

    @classmethod
    def accept(cls, equip, dep_name):
        cls.department[dep_name][equip.type].append(equip)

    @staticmethod
    def validate(val):
        if not val.isdigit() and val != "q":
            raise WarehouseValidationError("Значение должно быть числовым", " введите верное значение либо q")

    @classmethod
    def isexit(cls, val, checkdigit=True):
        if checkdigit:
            cls.validate(val)
        return val == "q"

    @classmethod
    def input(cls):
        while (True):
            try:
                a = input("Введите департамент: 1- менеджеры, 2 - аналитики  q - выход: ")
                if cls.isexit(a):
                    break
                if a == "1":
                    dep = 'managers'
                else:
                    dep = 'analytics'
                a = input("Что вы хотите добавить: принтер-1, сканер -2, ксерокс -3 ")
                if cls.isexit(a):
                    break
                model = input("Введите модель: ")
                if cls.isexit(model, checkdigit=False):
                    break
                cost = input("Введите цену: ")
                if cls.isexit(cost):
                    break
                count = input("Введите количество: ")
                if cls.isexit(count):
                    break
                if a == "1":
                    print_speed = input("Введите скорость печати: ")
                    if cls.isexit(print_speed):
                        break
                    eq = Printer(float(cost), int(count), model, int(print_speed))
                elif a == "2":
                    resolution = input("Введите разрешение: ")
                    if cls.isexit(resolution):
                        break
                    eq = Scanner(float(cost), int(count), model, int(resolution))
                else:
                    xerox_speed = input("Введите скорость ксерокса: ")
                    if cls.isexit(xerox_speed):
                        break
                    eq = Xerox(float(cost), int(count), model, int(xerox_speed))

                cls.accept(eq, dep)
            except WarehouseValidationError as e:
                print(e)

    @classmethod
    def display_info(cls):
        print("Информация о складе:")
        for key in cls.department:
            print(f"В  департаменте {key} имеется оборудование: ")
            for k in cls.department[key]:
                print(f" с типом {k}: ")
                for val in cls.department[key][k]:
                    print(val)


class Office_equipment(ABC):

    def __init__(self, cost, count, model, type):
        self.cost = cost
        self.count = count
        self.model = model
        self.type = type

    def __str__(self):
        return self.model + " по цене " + str(self.cost) + " в количестве " + str(self.count)


class Printer(Office_equipment):
    def __init__(self, cost, count, model, print_speed):
        super().__init__(cost, count, model, 'printer')
        self.print_speed = print_speed

    def __str__(self):
        return super().__str__() + " со скоростью печати " + str(self.print_speed)


class Scanner(Office_equipment):
    def __init__(self, cost, count, model, resolution):
        super().__init__(cost, count, model, 'scanner')
        self.resolution = resolution

    def __str__(self):
        return super().__str__() + " с разрешением  " + str(self.resolution)


class Xerox(Office_equipment):
    def __init__(self, cost, count, model, xerox_speed):
        super().__init__(cost, count, model, 'xerox')
        self.xerox_speed = xerox_speed

    def __str__(self):
        return super().__str__() + " со скоростью печати " + str(self.xerox_speed)


Warehouse.input()
Warehouse.display_info()
