from itertools import count

k = int(input(f"Введите нижнюю границу итератора k: "))

for el in count(k):
    if el > k * 10:
        break
    else:
        print(el)

from itertools import cycle

list_my = input(f"Введите элементы списка: ")

с = 0
for el in cycle(list_my):
    if с > 10:
        break
    print(el)
    с += 1
