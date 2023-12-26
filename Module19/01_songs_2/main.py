violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_track = int(input('Сколько песен выбрать? '))

sum_time = 0
for i in range(num_track):
    name_track = input(f'Название {i+1} песни: ')
    if name_track in violator_songs:
        sum_time += violator_songs.get(name_track)

print(f'Общее время звучания песен: {round(sum_time, 2)} минуты')