guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    come = input('Гость пришёл или ушёл? ').lower()

    if come == 'пришёл':
        name = input('Имя гостя: ')

        if len(guests) < 6:
            guests.append(name)
            print(f'Привет, {name}!')

        elif len(guests) >= 6:
            print(f'Прости, {name}, но мест нет.')


    elif come == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print(f'Пока {name}!')

    elif come == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
