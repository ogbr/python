f_obj = open("Quotations.txt")
i = 0
with open("Quotations.txt") as f_obj:
    for line in f_obj:
        print(line)
        print(f"Число слов в строке: {len(line.split())}")
        i += 1

print(f"\n Число строк равно: {i}")
f_obj.close()
