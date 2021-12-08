class Data:
    text = ''

    def __init__(self, text):
        Data.text= text

    @classmethod
    def get_int(cls):
        list_1 = cls.text.split('-')
        fin_list = list(map(int, list_1))
        cls.check_info(fin_list)
        return fin_list

    @staticmethod
    def check_info(list_1):
        for i in range(1, 32, 1):
            if list_1[0] == i:
                print("Формат дня корректен")
                break
        for k in range(1, 13, 1):
            if list_1[1] == k:
                print("Формат месяца корректен")
                break
        if list_1[2] == 2021:
            print("Формат года корректен")


text = '6-12-2021'
Data.text = text
print(Data.get_int())
print("--------------")
Data.text = ""
obj = Data(text)
print(obj.get_int())
