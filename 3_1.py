def my_func(n, m):
    """Следующие две строчки опциональные: выявляют ситуацию до самого деления"""
    if m == 0:
        raise ZeroDivisionError
    k = n / m
    return k


"""Ввод чисел"""
n = int(input("Введите первое число n: "))
m = int(input("Введите второе число m: "))
try:
    c = my_func(n, m)
    print(f"Результат деления n/m: {c:0.2f}")
except ZeroDivisionError:
    print("Ошибка ввода: делитель не может быть 0!")
