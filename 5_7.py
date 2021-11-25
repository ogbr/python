import json

with open("text_7.txt", 'r', encoding='utf-8') as f_obj:
    my_list = []
    res = 0
    i = 0
    my_dict = {}
    for line in f_obj:
        my_list = line.split()
        my_dict.update({my_list[0]: int(my_list[2]) - int(my_list[3])})
        if int(my_list[2]) - int(my_list[3]) > 0:
            res = res + int(my_list[2]) - int(my_list[3])
            i += 1
print([my_dict, {"средняя прибыль": res / i}])
data = [my_dict, {"средняя прибыль": res / i}]
with open("my_file.json", "w", encoding='utf-8') as write_f:
    json.dump(data, write_f)
