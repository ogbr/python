with open("Task5.txt", 'a', encoding='utf-8') as f_obj:
    f_obj.write('1 2 3 4 5 6 8')
with open("Task5.txt", 'r', encoding='utf-8') as f_obj:
    my_list = []
    for line in f_obj:
        my_list = list(map(int, line.split()))
    print(f" Набор чисел: {my_list}")
    print(f"Сумма элементов списка: {sum(my_list)}")
