def int_func(n):
    return n.title()


word = input("Введите слово: ")
print(int_func(word))
str_my = input("Введите строку из слов: ")
# print(int_func(str_my))
new_list = str_my.split(" ")
print(" ".join(list(map(int_func, new_list))))
