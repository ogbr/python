# pip install googletrans==4.0.0-rc1
from googletrans import Translator

res_obj = open("result.txt", 'a', encoding='utf-8')
translator = Translator()

with open("Task4.txt", mode="r", encoding='utf-8') as f_obj:
    for line in f_obj:
        result = translator.translate(line, src='en', dest='ru')
        res_obj.write(result.text + '\n')
