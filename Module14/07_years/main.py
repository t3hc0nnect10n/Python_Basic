# TODO здесь писать код
def three_digits(tmp_1, tmp_2):
    for num in range(tmp_1, tmp_2 + 1):
        num_1 = num // 1000
        num_2 = num // 100 % 10
        num_3 = num // 10 % 10
        num_4 = num % 10
        if (num_1 == num_2 == num_3) or (num_2 == num_3 == num_4) or \
                (num_3 == num_4 == num_1) or (num_1 == num_2 == num_4):
            print(num)


year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))

print(f'Года от {year_1} до {year_2} с тремя одинаковыми цифрами:')

three_digits(year_1, year_2)
