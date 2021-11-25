res = 0
i = 1
my_list = []
with open("Task3.txt", mode="r", encoding='utf-8') as f_obj:
    for line in f_obj:
        my_list = line.split()
        if float(my_list[1]) < 20000:
            print(my_list)
        res = res + float(my_list[1])
        i += 1
print(f"Средняя зарплата:  {res / i:0.2f}")
