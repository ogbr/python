from random import random


class DivideZeroValidationError(ZeroDivisionError):
    def __init__(self, errors):
        super().__init__("Ошибка!")
        self.errors = errors

    def __str__(self):
        return super().__str__() + "\t" + self.errors


class FindEr:
    def checkzerodiv(self, param_1, param_2):
        try:
            return round(int(param_1) / int(param_2), 2)
        except ZeroDivisionError:
            raise DivideZeroValidationError("На ноль делить нельзя")

    def get_check(self, param_1, param_2):
        try:
            res = self.checkzerodiv(param_1, param_2)
        except ZeroDivisionError as e:
            print(e)
        else:
            print(f"Программа отработала корректно. Результат деления {param_1} на {param_2}: {res}")
        finally:
            print("Программа завершена")


k = FindEr()
param_1 = input("Введите делимое:  ")
param_2 = input("Введите делитель:  ")
k.get_check(param_1, param_2)

# Вариант со случайной генерацией чисел

param_1 = round(random() * 10)
print(f"\nСлучайно сгенерированное делимое: {param_1}")
param_2 = round(random() * 10)
print(f"Случайно сгенерированный делитель: {param_2}")
k.get_check(param_1, param_2)
