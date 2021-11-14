my_list = [1, 3, 6, 2, 8, 9, 2]
print(f"Исходный массив: {my_list}")
n = int(input("Введите число: "))
my_list.append(n)
print(f"Массив с добавленным n: {my_list}")
k = len(my_list)
new_list = []
# while True:

while True:
    max = 0
    for m in my_list:
        if m > max:
            max = m
    new_list.append(max)
    my_list.remove(max)
    if len(new_list) == k:
        break
print(f"Массив после сортировки: {new_list}")
# Второй вариант
