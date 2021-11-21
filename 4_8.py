from itertools import count


def fact_my(n):
    list_my = []
    res = 1
    for el in count(1):
        if el > abs(n):
            break
        else:
            list_my.append(el)
            res = res * el
            yield res


n = int(input("Введите n: "))
for el in fact_my(n):
    print(el)
