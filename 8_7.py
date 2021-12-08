class ComplexNum:

    def __init__(self, im, real):
        self.im = im
        self.real = real

    def __add__(self, second_num):
        fin_real = self.real + second_num.real
        fin_im = self.im + second_num.im
        return ComplexNum(fin_real, fin_im)

    def __mul__(self, second_num):
        fin_real = self.real * second_num.real - self.im * second_num.im
        fin_im = self.real * second_num.im + second_num.real * self.im
        return ComplexNum(fin_real, fin_im)

    def __str__(self):
        return str(self.real) + str(self.im) + "j"


c_1 = ComplexNum(1, 5)
c_2 = ComplexNum(7, -6)
print(f"Результат сложения чисел: {c_1 + c_2}")
print(f"Результат умножения чисел: {c_1 * c_2}")
