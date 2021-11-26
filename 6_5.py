class Stationery:
    title = ''

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск маркером")


a = [Pen(), Pencil(), Handle()]
for k in a:
    k.draw()
