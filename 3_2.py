def my_func(name=input("Введите имя: "), surname=input("Введите фамилию: "),
            year=input("Введите год рождения: "), city=input("Введите город: "),
            phone=input("Введите телефон: "), mail=input("Введите e-mail: ")):
    """Вывод данных пользователя"""
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, "
          f"Город: {city}, телефон: {phone} ,e-mail {mail}")


#  return name, surname, name, surname, year, city, phone, mail
my_func()
