list_e = list(input("Ведите список элементов: "))
k = len(list_e)
print(f"Исходный список элементов: {list_e}")
print(f"Количество элементов в списке: {k}")
if k % 2 != 0:
    b = list_e.pop(k - 1)
    print(f"Последний элемент в нечетном списке: {b}")
i = 0
while i < (len(list_e) - 1):
    a = list_e[i]
    list_e[i] = list_e[i + 1]
    list_e[i + 1] = a
    i += 2

if k % 2 == 0:
    print(f"Список после обмена значений соседних элементов (четное кол-во): {list_e}")
elif k % 2 != 0:
    list_e.append(b)
print(f"Список после обмена значений соседних элементов (нечетное кол-во): {list_e}")
