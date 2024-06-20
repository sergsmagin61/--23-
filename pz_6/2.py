def max_of_lists(A, B):
    return [max(A[i], B[i]) for i in range(len(A))]

list_A = [3, 7, 1, 9, 4]

list_B = [5, 2, 8, 6, 10]


result_list = max_of_lists(list_A, list_B)
print("Новый список C:", result_list)
