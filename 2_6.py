i=1
list=[]
while True:
    name = input ("Введите наименование товара: ")
    price = input ("Введите цену товара: ")
    q = input("Введите количество товара: ")
    p = input("Введите единицы товара: ")

    dict={'название': name, 'ценa':price, 'количество':q, 'единицы':p}
    tuple=(i,dict)
    list.append(tuple)
    i+=1
    answer = input("Если хотите закончить ввод данных, нажмиту 'q' ")
    if answer=='q':
        break
i=0
while i<len(list):
    print(f"{list[i]}")
    i+=1
#аналитика
analgoods = {'название': [], 'ценa': [], 'количество': [], 'единицы': []}
for v in list:
    for k in v[1].keys():
        analgoods.update([(k, analgoods.get(k) + [v[1].get(k)])])
print(analgoods)