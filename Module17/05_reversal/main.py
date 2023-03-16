text = input('Введите строку: ')

letter_index = [i for i, letter in enumerate(text) if letter == 'h']
start = letter_index[0]
end = letter_index[len(letter_index) - 1] - 1

print(f'Развернутая последовательность между первым и последним h: {text[end:start:-1]}')