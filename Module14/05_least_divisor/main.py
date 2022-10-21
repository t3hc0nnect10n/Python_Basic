def lcd(a):
    lcd_num = 1

    for num in range(1, a + 1):
        if a % num == 0:
            lcd_num = num
        if lcd_num > 1:
            break
    return lcd_num


number = lcd(int(input('Введите число: ')))
print(f'Наименьший делитель, отличный от единицы: {number}')