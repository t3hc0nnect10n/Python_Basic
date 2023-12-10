def count_uppercase_lowercase(upp_low):
    count_upp = 0
    count_low = 0

    for i in upp_low:
        if i.isupper():
            count_upp += 1

        elif i.islower():
            count_low += 1

    return count_upp, count_low

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
