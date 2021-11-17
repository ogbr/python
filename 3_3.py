def my_func(a, b, c):
    res = list(map(int, [a, b, c]))
    res.remove(min(res))
    print(sum((res)))


a = input("Введите a: ")
b = input("Введите b: ")
c = input("Введите c: ")
my_func(a, b, c)
