#Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого положительного 
#числа K, а также их сумму S (K — входной, C и S — выходные параметры целого типа). С помощью 
#этой функции найти количество и сумму цифр для каждого из пяти данных целых чисел.


def digit_count_sum(K):
    str_K = str(K)
    return len(str_K), sum(map(int, str_K))

numbers = [456, 4567, 89012, 345678, 9012345]

for K in numbers:
    count, a = digit_count_sum(K)
    print(f"{K}: Количество цифр = {count}, Сумма цифр = {a}")