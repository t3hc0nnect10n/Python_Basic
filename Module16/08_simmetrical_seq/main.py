numbers = int(input('Количество чисел: '))
number_list = []
reverse_list = []

for _ in range(1, numbers + 1):
    num = int(input('Число: '))
    number_list.append(num)

print(f'Последовательность: {number_list}')
num_i = int(input('Нужно приписать чисел: '))

for i in range(num_i):
    reverse_list.append(number_list[i])

print(f'Сами числа: {reverse_list[::-1]}')