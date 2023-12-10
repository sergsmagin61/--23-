
#Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку S2


def replace_last_occurrence(S, S1, S2):
    return S.rsplit(S1, 1)[0] + S2 + S.rsplit(S1, 1)[-1]

# Пример использования
S = input("Введите строку S: ")
S1 = input("Введите подстроку S1: ")
S2 = input("Введите подстроку S2: ")

stroka = replace_last_occurrence(S, S1, S2)
print("Результат:", stroka)
