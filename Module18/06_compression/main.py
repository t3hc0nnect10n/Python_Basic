row = input('Введите строку: ')

temp = ''
broken = ''
new_string = ''

for i in row:
    if i != temp:
        broken += ' ' + i
        temp = i
    else:
        broken += i

for i in broken.split():
    new_string += str(i[0]) + str(len(i))

print(f'Закодированная строка: {new_string}')