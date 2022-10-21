def number_reverse(n):
    parts = str(n).split('.')
    parts[0] = ''.join(reversed(list(str(parts[0]))))
    parts[1] = ''.join(reversed(list(str(parts[1]))))
    return float(parts[0] + '.' + parts[1])


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

first_number_reverse = number_reverse(first_number)
second_number_reverse = number_reverse(second_number)
summ = first_number_reverse + second_number_reverse

print(f'Первое число наоборот: {first_number_reverse}')
print(f'Второе число наоборот: {second_number_reverse}')
print(f'Сумма: {summ}')