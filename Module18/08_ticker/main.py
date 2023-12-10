first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')

for shift in range(len(second_string)):
    if first_string == second_string:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        break
    second_string = second_string[1:] + second_string[0]
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')