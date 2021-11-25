f_obj = open("Quotation.txt", 'a')

while True:
    str_1 = input("Введите строку или для выхода набирите q: ")
    if str_1 == 'q':
        break
    else:
        f_obj.write(str_1)
        f_obj.write('\n')
        i = +1
f_obj.close()
