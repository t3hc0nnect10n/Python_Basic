vowels = 'ауоыиэяюёе'
text = input('Введите текст: ')
list_vowels = [i for i in text if i in vowels]

print(f'Список гласных букв: {list_vowels}'
      f'\nДлина списка: {len(list_vowels)}')