"""перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.
 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
файлов в папке test.
 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
 перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
 удалить файл test.txt."""


import os


"Задание 1"
path = 'D:\алгоритмизаци и програмирование\pz_11'
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        print(file)

"Задание 2"

total_size = 0
for dirpath, dirnames, filenames in os.walk('test'):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        file_size = os.path.getsize(filepath)
        total_size += file_size
        print(f"Размер файла {filename}: {file_size} байт")
print(f"Общий размер файлов {total_size} байт")

"Задание 3"
os.chdir('D:\алгоритмизаци и програмирование')
short_file = min(os.listdir('PZ_11'), key=len)
print("Файл с самым коротким именем: ", os.path.basename(short_file))

"Задание 4"
os.chdir('D:\алгоритмизаци и програмирование\pz_5')
for file in os.listdir():
     if file.endswith('.pdf'):
        os.startfile(file)
        break

"Задание 5"
os.chdir('D:\алгоритмизаци и програмирование')
os.remove('./test/test1/test.txt')

