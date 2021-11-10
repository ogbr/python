proceeds = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
profit = proceeds - cost
if proceeds > cost:
    print(f"Фирма работает с прибылью {profit} у.е. и рентабельностью составляет {profit*100 / proceeds:0.2f}%")

elif proceeds < cost:
    print(f"Фирма работает с убытками {-profit} у.е.")

ecount = int(input("Введите численность сотрудников: "))
print(f"Фирма работает с прибылью {profit / ecount} у.е в расчете на каждого сотрудника ")
