def digit_count_sum(K):
    str_K = str(K)
    return len(str_K), sum(map(int, str_K))

numbers = [456, 4567, 89012, 345678, 9012345]

for K in numbers:
    count, total = digit_count_sum(K)
    print(f"{K}: Количество цифр = {count}, Сумма цифр = {total}")
