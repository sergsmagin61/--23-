#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя. Посчитать количество полученных элементов
import re
filename = "Dostoevsky.txt"

with open('Dostoevsky.txt', "r", encoding="utf-8") as file:
        text = file.read()

def find_works(text):
    pattern = r'«(.+?)»'
    works = re.findall(pattern, text)
    return works

dostoyevsky_works = find_works(text)
print("Произведения Достоевского в файле:")
for work in dostoyevsky_works:
    print(work,";")

print(f"\n Всего найдено произведений: {len(dostoyevsky_works)}")
