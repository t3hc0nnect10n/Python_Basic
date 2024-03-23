# Вариант 1
def odd_numbers(i_number):
    odd_numbers_list = []
    for i_num in range(1, i_number + 1):
        if not i_num % 2 == 0:
            odd_numbers_list.append(i_num)

    return odd_numbers_list

number = int(input('Введите число: '))
print(f'Список из нечётных чисел от одного до N: {odd_numbers(number)}')

# Вариант 2
odd_numbers_list_2 = [i_num for i_num in range(1, number + 1) if not i_num % 2 == 0]
print(f'Список из нечётных чисел от одного до N: {odd_numbers_list_2}')