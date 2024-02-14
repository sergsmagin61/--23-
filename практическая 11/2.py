with open('text18-25.txt', 'r', encoding='utf-16') as file:
    content = file.read()

# количество букв в файле
letter_count = sum(1 for char in content if char.isalpha())

print("Содержимое файла:")
print(content)
print("Количество символов, принадлежащих к группе букв:", letter_count)

modified_content = content.replace('с', '')

# Разбиваем текст на строки для стихотворной формы
lines = modified_content.splitlines()

# стихотворная форма
stix = '\n'.join(lines)

# Создаем новый файл и записываем в него текст в стихотворной форме
with open('stix.txt', 'w', encoding='utf-8') as file:
    file.write(stix)

print("\nТекст успешно записан в файл stix.txt")
