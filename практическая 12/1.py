'''
1.Дана последовательность целых чисел. Поменять местами ее первую и
последнюю трети
'''
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

third_length = len(sequence) // 3

# Получаем первую, серединную и последнюю треть последовательности
first_third = sequence[:third_length]
middle_third = sequence[third_length:2*third_length]
last_third = sequence[2*third_length:]
new_sequence = last_third + middle_third + first_third

print(new_sequence)
