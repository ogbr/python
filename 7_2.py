from abc import ABC, abstractmethod


class Clothes(ABC):

    def get_operand1(self):
        pass

    def get_operand2(self):
        pass

    def calc(self):
        return self.get_operand1() + self.get_operand2()


class coat(Clothes):
    __V = 0

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, value):
        self.__V = value / 6.5

    def get_operand1(self):
        return self.__V

    def get_operand2(self):
        return 0.5


class suit(Clothes):
    __H = 0

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, value):
        self.__H = 2 * value

    def get_operand1(self):
        return self.__H

    def get_operand2(self):
        return 0.3


V = 10
H = 10
m1 = coat()
m1.V = V
print(f"Результат расчета расхода материала на пальто :{m1.calc():0.2f}")
m2 = suit()
m2.H = H
print(f"Результат расчета расхода материала на костюм :{m2.calc():0.2f}")
print(f"Результат расчета суммарного расхода: {m1.calc() + m2.calc():0.2f}")
