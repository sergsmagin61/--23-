def square_second_column(matrix):
    return [[row[i] ** 2 if i == 1 else 
            row[i] for i in range(len(row))] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = square_second_column(matrix)
for row in result_matrix:
    print(row)
