with open('3_26.txt', 'r') as file:
    lines = file.readlines()

#Парсинг
num_cells = int(lines[0].strip())
num_passengers = int(lines[1].strip())
requests = []

#обработка сток в исходном файле
for line in lines[2:]:
    start, end = map(int, line.strip().split())
    requests.append((start, end))

cells = [0] * num_cells
successful_passengers = 0
last_used_cell = -1

# тут обратботка всех заявок
for start, end in requests:
    for i in range(num_cells):
        if cells[i] < start:  #Если ячейка свободна
            cells[i] = end  #Занимаем ячейку
            successful_passengers += 1
            last_used_cell = i + 1
            break

print(successful_passengers, 'пассажиров сдали багаж')
print( 'Номер последней занятой ячейки:',last_used_cell)
