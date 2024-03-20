def sum_second_half(matrix):
    # Определение функции для нахождения суммы элементов второй половины матрицы
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Функция для вычисления суммы элементов второй половины матрицы
    def sum_half(start_row, start_col):
        return sum(sum(row[start_col:]) for row in matrix[start_row:])

    start_row = num_rows // 2
    start_col = num_cols // 2
    return sum_half(start_row, start_col)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = sum_second_half(matrix)
print("Сумма элементов второй половины матрицы:", result)
