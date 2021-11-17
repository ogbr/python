#
finel_res = 0
while True:
    str = input("Введите строку чисел, разделенных пробелом: ")
    list = str.split(' ')
    if 'q' in list:
        break
    else:
        # первый вариант
        # for k in list.copy():
        #     if not k.isdigit():
        #         list.remove(k)
        # print(f"Численный массив: {list}")
        # amount=sum(map(int,list))

        # второй вариант
        amount = sum(map(lambda a: float(a) if a.isdigit() else 0, list))
        finel_res += amount
        print(f" Итоговая сумма: {finel_res}, промежуточная сумма: {amount}")
