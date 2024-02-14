'''
1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной 
последовательности из целых положительных и отрицательных чисел. Сформировать 
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
обработку элементов:
Элементы первого и второго файлов:
Элементы после сортировки:
Количество элементов:
Минимальный элемент кратный 2:
Максимальный элемент кратный 5:
'''

# создание 2х файлов

with open('file1.txt', 'w') as file1, open('file2.txt', 'w') as file2:
    sequence1 = [1, 5, 8, 12, 17, -3, -7, -10, -15, -20]
    sequence2 = [-2, 4, -6, 8, -10, 3, 6, 9]

    file1.write(','.join(map(str, sequence1)))
    file2.write(','.join(map(str, sequence2)))

with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    
    # формируем списки элементов
    elements1 = list(map(int, file1.read().split(',')))
    elements2 = list(map(int, file2.read().split(',')))


all_elements = elements1 + elements2

sorted_elements = sorted(all_elements)

# Общее количество элементов в списке:
num_elements = len(sorted_elements)

min_element_multiple_of_2 = min(x for x in sorted_elements if x % 2 == 0)

max_element_multiple_of_5 = max(x for x in sorted_elements if x % 5 == 0)

with open('result.txt', 'w',) as result_file:
    result_file.write("Элементы первого и второго файлов:\n")
    result_file.write(f"File 1: {elements1}\n")
    result_file.write(f"File 2: {elements2}\n\n")

    result_file.write("Элементы после сортировки:\n")
    result_file.write(f"Sorted Elements: {sorted_elements}\n\n")

    result_file.write(f"elements: {num_elements}\n")
    result_file.write(f"min_element_krat_2: {min_element_multiple_of_2}\n")
    result_file.write(f"Максимальный элемент кратный 5: {max_element_multiple_of_5}\n")
