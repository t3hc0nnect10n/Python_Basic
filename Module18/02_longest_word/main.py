text = input('Введите строку: ')

words = text.split()
max_word = max(words, key=len)
max_len = len(max_word)

print(f'Самое длинное слово: {max_word}')
print(f'Длина этого слова: {max_len}')