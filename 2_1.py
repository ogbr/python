list_example = [1, 2.05, "example", (1, 2), [12, 3, 'a', 's'], 3 + 5j,
                'фио', None, False, True, '!', {1, 2, 3}, {'n': 600}, b"olga", ZeroDivisionError()]
print(list_example)
i = 0
while i < len(list_example):
    print(type(list_example[i]))
    i += 1
