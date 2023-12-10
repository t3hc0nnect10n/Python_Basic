while True:
    ip_address = input('Введите IP: ').split('.')

    if len(ip_address) != 4:  # проверка на длину IP адреса
        print('Адрес — это четыре числа, разделённые точками.')

    else:
        for i in ip_address:

            if not i.isdigit():  # проверка на целое число
                print(f'{i} — это не целое число.')
                break

            elif int(i) > 255: # проверка не превышает ли число допустимое значение '255'
                print(f'{i} превышает 255.')
                break

        else:
            print('IP-адрес корректен.')
            break
