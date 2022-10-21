def sum_dif():
    def is_number(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def summ(number_n):
        num = list(str(number_n))
        num = list(map(int, num))
        return sum(num)

    def dif():
        return len(str(number))

    number = str(input('Введите целое, положительное число: '))

    if is_number(number):
        if int(number) >= 0:
            summ_n = summ(number)
            dif_n = dif()
            difference = abs(summ_n - dif_n)
            print(f'Сумма чисел: {summ_n}')
            print(f'Количество цифр в числе: {dif_n}')
            print(f'Разность суммы и количества цифр: {difference}')
        elif int(number) < 0:
            print('\nОшибка! Введите положительное число!\n')
            sum_dif()
    elif not is_number(number):
        print('\nОшибка! Введите целое число!\n')
        sum_dif()


sum_dif()