row = input('Введите строку: ')

new_string = ''

for i in row:

    if not len(new_string):
           new_string = i + '1'

    else:

        if i == new_string[-2]:
            new_string = '{}{}'.format(new_string[:-1], int(new_string[-1]) + 1)
        else:
            new_string = '{}{}{}'.format(new_string, i, '1')

print(f'Закодированная строка: {new_string}')