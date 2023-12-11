# Функция "latin" проверяет пароль на наличие латинских букв
def latin(text):
    count = 0
    for i in text:
        if i.encode().isalpha():
            count += 1

    if count >= 1:
        return True
    else:
        return False

# Функция "low" проверяет пароль на наличие прописной буквы
def low(text):
    count = 0
    for i in text:
        if i.islower():
            count += 1

    if count >= 1:
        return True
    else:
        return False

# Функция "upp" проверяет пароль на наличие заглавной буквы
def upp(text):
    count = 0
    for i in text:
        if i.isupper():
            count += 1

    if count >= 1:
        return True
    else:
        return False

# Функция "digit_min_three" проверяет пароль на наличие минимум трёх цифр
def digit_min_three(text):
    count = 0
    for i in text:
        if i.isdigit():
            count += 1

    if count >= 3:
        return True
    else:
        return False

# В цикле проверяется выполнение условий к требованиям сложности пароля
while True:
    password = input('Придумайте пароль: ')

    if (len(password) > 8) and latin(password) and digit_min_three(password) and low(password) and upp(password):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')