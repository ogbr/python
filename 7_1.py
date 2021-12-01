class Matrix:
    __ownList = [[], [], []]

    def __init__(self, a):
        self.__ownList = a

    def get_own_list(self):
        return self.__ownList

    def __str__(self):
        a = self.get_own_list()
        i = 0
        res = ""
        while i < len(a):
            res += "\t".join(map(str, a[i])) + "\n"
            i += 1
        return res

    def __add__(self, second_matrix):
        a = self.get_own_list()
        b = second_matrix.get_own_list()
        res = [list(map(lambda a, b: a + b, a[0], b[1])) for a in zip(a, b)]
        return Matrix(res)


m1 = Matrix([[1, 2, 3], [1, 2, 4], [5, 9, 2]])
m2 = Matrix([[1, 2, 7], [3, 2, 7], [6, 7, 9]])
print(f"{m1}\t+\n{m2}\t=\n{m1 + m2}")
