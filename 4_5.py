from functools import reduce

my_list = [el for el in range(100, 1000 + 1) if el % 2 == 0]

print(my_list)


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(reduce(my_func, my_list))

# вариант 2
print(reduce(lambda a, b: a * b, my_list))
