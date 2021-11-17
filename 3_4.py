"""ПЕРВЫЙ вариант"""


def my_func(x, y):
    res = 1 / (x ** abs(y)) if y < 0 else x ** y
    print(f"Результат возведения x в степень y: {res:0.2f}")


x = float(input("Введите действительное положительное число x: "))
y = int(input("Введите целое отрицательное число y: "))
my_func(x, y)

"""ВТОРОЙ вариант"""


def my_function(x, y):
    res = x
    i = 1
    while (i < abs(y)):
        res = res * x
        i += 1
    return res


res = my_function(x, y)
if y < 0:
    print(f"Результат возведения x в степень y: {(1 / res):0.2f}")
else:
    print(f"Результат возведения x в степень y: {res:0.2f}")

"""ТРЕТИЙ вариант"""
r = 1
for i in range(abs(y)):
    r = x * r
    print(r if y > 0 else 1 / r)
