#2.Составить генератор (yield), который выводит из строки только цифры.
input_string = "abc123def456gh79080i"
digits = (char for char in input_string if char.isdigit())
for digit in digits:
    print(digit)
    result = ''.join(digits)
print(result)