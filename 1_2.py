sec = int(input("Введите время в секундах"))
#вариант 1
m = sec // 60
h = sec // 3600
s = sec - h * 3600 - m * 60
print(f"{h:02d}:{m:02d}:{s:2d}")
#вариант 2
print(f"{sec // 3600:02d}:{sec // 60:02d}:{sec%60:02d}")