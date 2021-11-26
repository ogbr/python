class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("Машина " + self.name + " c цветом " + self.color + " поехала")

    def stop(self):
        print("Машина " + self.name + " остановилась")

    def turn(self, direction):
        print("Машина " + self.name + " повернула " + direction)

    def show_speed(self):
        print(f"Скорость машины: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Вы превысили скорость!")


class SportCar(Car):
    cilinder_number = 8

    def __init__(self, speed, color, name, cilinder_number):
        super().__init__(speed, color, name)
        self.cilinder_number = cilinder_number

    def go(self):
        super().go()
        print(f"У двигателя  {self.cilinder_number}  цилиндров")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Вы превысили скорость!")


class PoliceCar(Car):
    police_district = 'Newskiy'

    def __init__(self, speed, color, name, district):
        super().__init__(speed, color, name)
        self.police_district = district
        self.is_police = True

    def go(self):
        super().go()
        print("Машина поехала в  полицейский участок " + self.police_district)


a = TownCar(100, "зеленая", "Волга")
a.go()
a.turn(direction='направо')
a.show_speed()
a.stop()

b = SportCar(200, "желтая", "Феррари", 10)
b.go()
b.turn(direction='налево')
b.show_speed()
b.stop()

с = WorkCar(90, "красный", "трактор")
с.go()
с.show_speed()
с.stop()

d = PoliceCar(90, "синяя", "Мазда", "Невского района")
d.go()
d.show_speed()
d.stop()
