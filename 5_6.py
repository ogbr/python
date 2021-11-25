with open("Task6.txt", 'r', encoding='utf-8') as f_obj:
    my_dict = {}
    for line in f_obj:
        my_list1 = line.split()
        digs = [my_list1[1].split("("), my_list1[2].split("("), my_list1[3].split("(")]
        digs = list(map(lambda x: int(x[0]) if x[0].isdigit() else 0, digs))
        # print(digs)
        my_dict.update({my_list1[0].replace(":", ""): sum(digs)})
print(my_dict)

# вариант 2
import re

lst = ["Информатика: 100(л) 50(пр) 20(лаб).", "Физика: 30(л) — 10(лаб)", "Физкультура: — 30(пр) —"]
r = {}
for line in lst:
    kv = line.split(":")
    dv = [int(v) for v in map(lambda x: re.sub("[^0-9]", "", x), kv[1].split("(")) if v.isdigit()]
    r.update({kv[0]: sum(dv)})
print(f"\n Второй вариант:  {r}")
