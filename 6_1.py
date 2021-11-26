import time as tm


class TrafficLight:
    __color = ''

    def running(self, color, time):
        if color == 'red':
            print("\033[31m {}".format(color))
            tm.sleep(time)
        if color == 'yellow':
            print("\033[33m {}".format(color))
            tm.sleep(time)
        if color == 'green':
            print("\033[32m {}".format(color))
            tm.sleep(time)


i = 0
while True:
    a = TrafficLight()
    a.running("green", 7)

    b = TrafficLight()
    b.running("yellow", 2)

    c = TrafficLight()
    c.running("red", 7)

    b = TrafficLight()
    b.running("yellow", 2)

    i += 1
    if i > 2:
        break
