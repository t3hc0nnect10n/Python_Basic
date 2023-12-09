while True:
    password = input('Придумайте пароль: ')
    if (len(password) >= 8) and (password.isalnum()) and (password.islower()) == (password.isupper()):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')