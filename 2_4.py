string = input("Введите строку из нескольких слов, разделённых пробелами: ")
print(f"Исходное форматирование: {string}")

words = string.split(' ')
# вариант 1
i = 0
while i < len(words):
    word = words[i]
    if len(words[i]) > 10:
        word = word[:10]
    print(f"{i + 1}" + ")" + word)
    i += 1
# вариант 2
for i, v in enumerate(words, 1):
    print(i, v)
