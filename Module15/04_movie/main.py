films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorit_list = []
user_enter = int(input('Сколько фильмов хотите добавить? '))
for i in range(1, user_enter + 1):
    film_name = input('Введите название фильма: ')
    if film_name in films:
        favorit_list.append(film_name)
    else:
        print(f'Ошибка: фильма {film_name} у нас нет :(')

result = ', '.join(favorit_list)
print(f'Ваш список любимых фильмов: {result}')
