from sys import argv

script_name, a, b, c = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", a)
print("Ставка в час: ", b)
print("Премия: ", c)
my_list = [a, b, c]
# map(int(),my_list)
print(my_list)
fin_list=list(map(float,filter(lambda a: a.isdigit(), my_list)))
print(fin_list)
if len(fin_list)<3:
    print ("Некорректно заданы исходные параметры!")
else:
    res = fin_list[0]*fin_list[1]+fin_list[2]
    print(f"Зарплата с учетом премии: {res}")
