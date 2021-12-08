class FindWrongValue:
    class IntListValidationError(ValueError):
        def __init__(self):
            super().__init__("Это не число!")

    @classmethod
    def append(cls, lst, n):
        try:
            lst.append(int(n))
        except ValueError:
            raise cls.IntListValidationError()

    def get_check(self):
        fin_list = []
        while True:
            n = input("Введите любой символ или stop, чтобы выйти из программы: ")
            if n == 'stop':
                break
            else:
                try:
                    self.append(fin_list, n)
                except ValueError as e:
                    print(e)
        print(f"Программа отработала корректно. Сформирован финальный список {fin_list}")


k = FindWrongValue()
k.get_check()
