class Road:
    _length = 0
    _width = 0

    def __init__(self, alen, awidth):
        self._length = alen
        self._width = awidth
        print(Road._length, Road._width)
        print(self._length, self._width)

    def get_calculation_mass(self, mass, thickness):
        print(self._length * self._width * mass * thickness / 1000)


a = Road(5000, 20)
a.get_calculation_mass(25, 5)
